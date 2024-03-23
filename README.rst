harmonize
=========

Based on Harmonize by nvllsvm https://github.com/nvllsvm/harmonize

Create and synchronize transcoded copies of audio folders.

* Can transcodes FLAC, M4A and MP3 files to Opus or MP3 with tags
* Hardlink, symbolic link or Copy everything else as-is
* Parallelized
* Additional runs synchronize changes since the initial run
* Configurable encoders

Changes from nvllsvm's version
------------------------------
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

Recommended usage via docker compose
=====================================

Build Locally
-------------
* No premade container is available so you will need to build it yourself
* Download the contents of the repository
* Open the location in a terminal

.. code::

    docker compose build

Setup docker compose file
-------------------------

* For a complete docker compose file with all options see the included docker-compose.yml

Minimal docker compose file

.. code::

    services:
      harmonize:
        container_name: harmonize
        build: 
          context: ./
          dockerfile: Dockerfile
        user: 1000:1000         # Should match your user
        environment:
          PUID: 1000            # Should match your user
          PGID: 1000            # Should match your user group
        volumes:                # To use Hardlinks all files must be on the same mount point, Bind locations will not work.
          - /mnt:/mnt           # mount_location:virtual_location # The virtual location must match the mount location
        command: 
          - "/mnt/Music"        # absolute path to source folder, must be inside the mapped volume above
          - "/mnt/Music-opus"   # absolute path to target folder, must be inside the mapped volume above

Run the docker container
------------------------

* Be sure to build it first
* Be sure to setup the paths in the docker compose file

.. code::

    docker compose up
    
To run in the background

.. code::

    docker compose up -d
    

Direct script usage
===================

.. code::

    usage: harmonize [-h] [--codec {mp3,opus}] [-n NUM_PROCESSES] [-q]                                                                                              
                     [--hardlink {True,False}] [--softlink {True,False}]
                     [--cleanup {True,False}] [--convflac {True,False}]
                     [--convm4a {True,False}] [--convmp3 {True,False}] [--version]
                     [--exclude PATTERN]
                     source target
    
    positional arguments:
      source                    Source directory
      target                    Target directory
    
    options:
      -h, --help                show this help message and exit
      --codec {mp3,opus}        codec to use for output. encoder configuration may be
                                specified as additional arguments to harmonize
      -n NUM_PROCESSES          Number of processes to use
      -q, --quiet               suppress informational output
      --hardlink {True,False}   use hardlinks instead of copying the extra files
      --softlink {True,False}   use symbolic links instead of copying the extra files
      --cleanup {True,False}    remove files not found in the source
      --convflac {True,False}   convert flac files to output codec
      --convm4a {True,False}    convert m4a files to output codec
      --convmp3 {True,False}    convert mp3 files to output codec
      --version                 show program's version number and exit
      --exclude PATTERN         ignore files matching this pattern
