
unit-test:
	nosetests

run-testbed:
	@echo "Running quick testbed test..."
	python organize.py --directory music_files/ --backup backup_files/

clean-testbed:
	@echo "Removing testbed files and directories..."
	rm -rf music_files
	rm -rf backup_files

create-testbed: clean-testbed
	@echo "Generating directories..."
	mkdir music_files
	mkdir backup_files
	@echo "Creating empty test mp3 files..."
	@touch music_files/testfile1.mp3
	@touch music_files/testfile2.mp3
	@touch music_files/testfile3.mp3
	@touch music_files/testfile4.mp3
	@touch music_files/testfile5.mp3
	@touch music_files/testfile6.mp3
	@touch music_files/testfile7.mp3
	@touch music_files/testfile8.mp3
	@touch music_files/testfile9.mp3
	@touch music_files/testfile10.mp3
	@echo "Creating empty non-mp3 files..."
	@touch music_files/nomatch1.txt
	@touch music_files/nomatch2.txt
	@touch music_files/nomatch3.txt
	@touch music_files/nomatch4.txt
	@touch music_files/nomatch5.txt
	@echo "Done."

