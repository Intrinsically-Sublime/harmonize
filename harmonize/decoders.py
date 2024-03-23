import asyncio
import contextlib
import logging
import os

LOGGER = logging.getLogger(__name__)


@contextlib.asynccontextmanager
async def flac(path):
    """Decode a FLAC file

    Decodes through any errors.

    :param pathlib.Path path: The FLAC file path
    """
    read_pipe, write_pipe = os.pipe()

    proc = await asyncio.create_subprocess_exec(
        'flac', '-csd', path,
        stdout=write_pipe,
        stderr=asyncio.subprocess.PIPE)

    os.close(write_pipe)

    yield read_pipe
    await proc.wait()
    # Decode errors, many are non-fatal, but may indicate a problem
    stderr = await proc.stderr.read()
    if proc.returncode:
        LOGGER.info('ERROR DECODING FLAC %s', proc.returncode)
    if stderr:
        LOGGER.warning('ERROR DECODING FLAC "%s"', stderr)


@contextlib.asynccontextmanager
async def mp3(path):
    """Decode an MP3 file

    :param pathlib.Path path: The MP3 file path
    """
    read_pipe, write_pipe = os.pipe()

    proc = await asyncio.create_subprocess_exec(
        'ffmpeg', '-i', path, '-f', 'wav', '-',
        stdout=write_pipe,
        stderr=asyncio.subprocess.PIPE)

    os.close(write_pipe)

    yield read_pipe
    await proc.wait()
    # Decode errors may are non-fatal, but may indicate a problem
    stderr = await proc.stderr.read()
    if proc.returncode:
        LOGGER.info('ERROR DECODING MP3 %s', proc.returncode)


@contextlib.asynccontextmanager
async def mp4(path):
    """Decode an M4A file

    :param pathlib.Path path: The M4A file path
    """
    read_pipe, write_pipe = os.pipe()

    proc = await asyncio.create_subprocess_exec(
        'ffmpeg', '-i', path, '-f', 'wav', '-',
        stdout=write_pipe,
        stderr=asyncio.subprocess.PIPE)

    os.close(write_pipe)

    yield read_pipe
    await proc.wait()
    # Decode errors may are non-fatal, but may indicate a problem
    stderr = await proc.stderr.read()
    if proc.returncode:
        LOGGER.info('ERROR DECODING M4A %s', proc.returncode)


