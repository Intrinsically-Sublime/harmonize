Changelog
=========

1.1.0 (2024-03-23)  Intrinsically-Sublime First Release
------------------
* Add hardlink option (instead of copying the extra files)
* Add symbolic link option (instead of copying the extra files)
* Add m4a (mp4) as input source for transcoding
* Add mp3 as input source for transcoding (from nvllsvm's branch)
* Make transcoding flac optional
* Make transcoding m4a optional
* Make transcoding mp3 optional
* Make sanitizing optional (allows syncing multiple sources to one target)
* Make variables available as Docker Environment Variables
* Add docker compose example with all variables
* Remove "raise asyncio.subprocess.CalledProcessError" since asyncio.subprocess doesn't have CalledProcessError
* Add primitive error reporting in place of above

NVLLSVM Versions
================

1.0.2 (2020-07-02)
------------------
* Read source mtime only once as source may change during transcode

1.0.1 (2019-11-23)
------------------
* Fix double .. in file extension

1.0.0 (2019-11-23)
------------------
* Add opus support
* Make encoders configurable
* Refactor

0.4.0 (2019-10-19)
------------------
* Add `--quiet` flag
* Copy file mode
* Add __main__
* Misc cleanup

0.3.2 (2018-10-05)
------------------
* Stop chowning /source folder (Dominik)
* Use `.temp` extension for temporary filenames (Dominik)
* Log error when file already exists (Dominik)

0.3.1 (2018-08-17)
------------------
* Revert app import exposure

0.3.0 (2018-08-17)
------------------
* Drastically reduce memory consumption by simultaneously decoding and encoding

0.2.2 (2018-06-17)
------------------
* Fail upon decoding corrupt FLAC files
* Ignore tagging errors

0.2.1 (2018-06-15)
------------------
* Remove unexpected directories from target

0.2.0 (2018-06-10)
------------------
* Replace FFmpeg with LAME and mutagen

0.1.5 (2018-05-19)
------------------
* Log copies and deletes

0.1.4 (2018-05-14)
------------------
* Add num processes flag
* Fix parallelization for small folders

0.1.3 (2018-05-14)
------------------
* Add additional logging

0.1.2 (2018-05-14)
------------------
* Add MANIFEST

0.1.1 (2018-05-14)
------------------
* Removed external Python package dependencies
* Refactored

0.1.0 (2018-05-13)
------------------
* Initial release
