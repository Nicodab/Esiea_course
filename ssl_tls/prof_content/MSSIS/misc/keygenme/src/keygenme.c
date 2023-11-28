#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>


#define CHK_EQ_NULL(x, label)		do{if (NULL == (x)) goto label;} 	while(0)
#define CHK_NEQ_VALUE(x, v, label) 	do{if ((v) != (x)) goto label;}	 	while(0)
#define CHK_NLE_VALUE(x, v, label) 	do{if ((v) < (x)) goto label;} 		while(0)
#define CHK_NGE_VALUE(x, v, label) 	do{if ((v) > (x)) goto label;} 		while(0)


#define SERIAL_SZ 			9 // XXXX-YYYY -> 4+1+4
#define VERIFY_SUCCESS 		0x00
#define VERIFY_FAILURE 		0x01
#define VERIFY_BAD_FORMAT 	0x02
#define VERIFY_BAD_LENGTH 	0x03
#define VERIFY_ERR_MEMORY 	0x04
#define VERIFY_BAD_INPUT 	0x05

#define CHECKSUM_PART_1_BYTE 		0x10
#define CHECKSUM_PART_1_INT 		0x687E7076


int32_t verify_serial(int8_t *serial)
{
	int32_t ret;
	int32_t i;
	uint8_t checksum_byte;
	uint32_t checksum_int;


	/* *** 00. initialisation *** */
	ret = VERIFY_FAILURE;
	checksum_byte = 0;
	checksum_int = 0;


	/* *** 01. check input *** */
	ret = VERIFY_BAD_INPUT;
	CHK_EQ_NULL(serial, cleanup);


	/* *** 02. check length *** */
	ret = VERIFY_BAD_LENGTH;
	CHK_NEQ_VALUE(strlen(serial), SERIAL_SZ, cleanup);
	printf("[+] serial length ok\n");


	/* *** 03. check serial format *** */
	// SERIAL_FMT = [A-Z][A-Z][A-Z][A-Z]-[0-9][0-9][0-9][0-9]
	ret = VERIFY_BAD_FORMAT;
	for (i = 0; i < 4; i++)
	{
		CHK_NGE_VALUE(serial[i], 'A', cleanup);
		CHK_NLE_VALUE(serial[i], 'Z', cleanup);
	}
	CHK_NEQ_VALUE(serial[i], '-', cleanup);
	for (i = 5; i < 9; i++)
	{
		CHK_NGE_VALUE(serial[i], '0', cleanup);
		CHK_NLE_VALUE(serial[i], '9', cleanup);
	}
	printf("[+] format serial verified !\n");


	/* *** 04. check serial validity *** */
	ret = VERIFY_FAILURE;
	// CHECKSUM_BYTE
	for (i = 0; i < SERIAL_SZ; i++)
	{
		if (4 == i)
		{
			continue;
		}
		checksum_byte ^= serial[i];
	}
	// CHECKSUM_INT
	for (i = 0; i < SERIAL_SZ; i++)
	{
		if (4 == i)
		{
			continue;
		}
		checksum_int ^= ( ((serial[i] & 0xFF) << 24) | ((serial[i+1] & 0xFF) << 16) | ((serial[i+2] & 0xFF) << 8) | (serial[i+3] & 0xFF) ) & 0xFFFFFFFF;
		i+=4;
	}
	// check all checksums
	CHK_NEQ_VALUE(checksum_byte, CHECKSUM_PART_1_BYTE, cleanup);
	CHK_NEQ_VALUE(checksum_int, CHECKSUM_PART_1_INT, cleanup);


	ret = VERIFY_SUCCESS;
cleanup:
	switch(ret)
	{
		case VERIFY_BAD_FORMAT:
			fprintf(stderr, "[-] wrong serial format\n");
			break;
		case VERIFY_BAD_LENGTH:
			fprintf(stderr, "[-] wrong serial length\n");
			break;
		case VERIFY_BAD_INPUT:
			fprintf(stderr, "[-] input mus't be NULL\n");
			break;
		case VERIFY_FAILURE:
			fprintf(stderr, "[-] wrong serial\n");
			fprintf(stderr, "    -> [checksum byte]  expected : %02X       | got : %02X\n", CHECKSUM_PART_1_BYTE, checksum_byte);
			fprintf(stderr, "    -> [checksum int]   expected : %08X | got : %08X\n", CHECKSUM_PART_1_INT, checksum_int);
		default:
			break;
	}
	return ret;
}


static inline void zeroize(void *memory, size_t sz)
{
	volatile uint8_t *p = memory;
	while (p < (uint8_t *)memory + sz)
		*p++ = 0;
}


int main(int argc, char *argv[])
{
	int32_t ret;
	int8_t serial[SERIAL_SZ];

	ret = VERIFY_FAILURE;

	if (2 == argc)
	{
		strcpy(serial, argv[1]);

		ret = verify_serial(serial);
		if (VERIFY_SUCCESS != ret)
		{
			fprintf(stderr, "[-] bad serial\n");
		}
		else
		{
			printf("[+] authorization granted, welcome !\n");
		}
	}
	else
	{
		fprintf(stderr, "usage : %s <serial>\n", argv[0]);
	}

	return ret;
}
