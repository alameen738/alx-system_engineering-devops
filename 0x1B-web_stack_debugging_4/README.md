# Web Stack Debugging #4

## Description

This project is part of a series of web stack debugging tasks. In this particular task, we encountered an issue with a web server where the HTTP request to the server returns a `500 Internal Server Error`. The goal is to identify the root cause of this issue and implement a fix.

## Issue

When making an HTTP request to the server, it returns a `500 Internal Server Error`.

## Steps Taken

1. **Investigation**: 
    - Checked server logs (`/var/log/nginx/error.log`) for any error messages.
    - Found an error related to a missing file: 
      ```
      FileNotFoundError: [Errno 2] No such file or directory: '/etc/nginx/sites-available/default'
      ```
2. **Resolution**:
    - Discovered that the Nginx configuration file was referencing a non-existent file.
    - Updated the Nginx configuration file to point to the correct file location.
    - Reloaded Nginx to apply the changes.
3. **Verification**:
    - Made a test HTTP request to the server to ensure the issue was resolved.
    - Confirmed that the server now returns the expected response without any errors.

## How to Use

To replicate the issue and test the fix:

1. Make an HTTP request to the server endpoint.
2. Observe the returned response.
3. After applying the fix, repeat step 1 and ensure that the server responds without any errors.

## Additional Notes

- This README assumes familiarity with web server configuration and debugging techniques.
- For more details on the debugging process, refer to the comments in the related configuration files and logs.

## Resources

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Stack Overflow](https://stackoverflow.com/) and other online communities for troubleshooting assistance.
