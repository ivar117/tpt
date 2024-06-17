install:
	chmod +x tpt.py
	cp -f tpt.py /usr/local/bin/tpt
	mkdir -p /usr/local/share/tpt/
	cp -f config.ini /usr/local/share/tpt/
uninstall:
	rm -f /usr/local/bin/tpt
	rm -rf /usr/local/share/tpt/
