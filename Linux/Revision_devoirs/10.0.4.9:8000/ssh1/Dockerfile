FROM alpine:latest
RUN apk add --no-cache openssh && \
	ssh-keygen -A && \
	adduser --disabled-password --gecos "" ctf && \ 
	echo "root:easyssh" | chpasswd && \
	echo "ctf:easyssh" | chpasswd
COPY flag.txt /home/ctf/so_much_to_explore/maybe_here/
COPY sshd_banner sshd_config /etc/ssh/
COPY motd /etc
USER root
RUN	mkdir -p /home/ctf/a_directory /home/ctf/another_directory /home/ctf/so_much_to_explore/maybe_here /home/ctf/so_much_to_explore/or_here && \
	echo "you should continue to search" > /home/ctf/another_directory/file && \
	chown -R root:ctf /home/ctf && \
	chmod -R ug=rX,o= /home/ctf && \
	rm -f /usr/bin/scp /usr/bin/sftp /usr/bin/nc && \
	chmod o=rx /var/tmp /dev/shm /dev/mqueue /tmp
ENTRYPOINT []
CMD ["/usr/sbin/sshd", "-D"]
EXPOSE 22
