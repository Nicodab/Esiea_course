; =============== S U B R O U T I N E =======================================

; Attributes: bp-based frame

sub_401000      proc near               ; CODE XREF: sub_401060+3↓p

var_198         = dword ptr -198h
var_194         = dword ptr -194h
var_4           = dword ptr -4

                push    ebp
                mov     ebp, esp
                sub     esp, 198h
                mov     eax, ___security_cookie
                xor     eax, ebp
                mov     [ebp+var_4], eax
                mov     [ebp+var_198], 0
                jmp     short loc_40102E
; ---------------------------------------------------------------------------

loc_40101F:                             ; CODE XREF: sub_401000+4A↓j
                mov     eax, [ebp+var_198]
                add     eax, 1
                mov     [ebp+var_198], eax

loc_40102E:                             ; CODE XREF: sub_401000+1D↑j
                cmp     [ebp+var_198], 64h
                jnb     short loc_40104C
                mov     ecx, [ebp+var_198]
                mov     edx, [ebp+var_198]
                mov     [ebp+ecx*4+var_194], edx
                jmp     short loc_40101F
; ---------------------------------------------------------------------------

loc_40104C:                             ; CODE XREF: sub_401000+35↑j
                mov     ecx, [ebp+var_4]
                xor     ecx, ebp
                call    @__security_check_cookie@4 ; __security_check_cookie(x)
                mov     esp, ebp
                pop     ebp
                retn
sub_401000      endp

; ---------------------------------------------------------------------------
