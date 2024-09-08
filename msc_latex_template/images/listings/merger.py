def wait_until_files_closed(files: list[str], wait: float) -> bool:
    """Blocks until all the provided files are closed or until the provided timetout ends.

    Parameters
    ----------
    files: List[str]
        The list of files to watch.
    wait: float
        The maximum time allowed to block in seconds.

    Returns
    -------
    bool:
        True if exited after timeout expired. False otherwise.
    """
    timeout_seconds = wait
    start_time = time.time()

    while time.time() - start_time < timeout_seconds:
        all_closed = True
        for file_path in files:
            # Use grep to check if the specific file is still open
            result = subprocess.run(['lsof', '|', 'grep', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stdout:
                logging.debug(f"The file {file_path} is still open.")
                all_closed = False
                break  # If any file is still open, break and retry after a pause
            else:
                logging.debug(f"The file {file_path} is now closed.")

        if all_closed:
            return True

        time.sleep(1)  # Wait for 1 second before trying again

    return False