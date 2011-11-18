This uses echonest api to filter my iTunes library or a given folder based on the music I like.

Nothing complicated..

### Some Notes

* It assumes that file names are properly named (like 'Artist-Title.mp3' or 'Artist-Album-Title.mp3'
* If ID3 tags are not properly named or they are empty, then it uses the metadata from the file name itself as shown above

### Installation

Make sure that you have ffmpeg installed on your system and you do also need storm, id3reader and pyechonest python libraries. And then:

    rake


