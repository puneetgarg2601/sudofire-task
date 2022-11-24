# Points:

- I have created 2 .bat files. We have to create two tasks for both the .bat files

  - 1. First .bat file is pgres_to_file.bat . The file is used to take the backup of postgres database to the file location.
  - 2. Second one is file_to_s3.bat . The file is used to copy the files in file location to aws s3 location. Also in this bat file the URI stands for the unique resource identifier of the bucket where we want to dump our data.

## Note

```
Here i have assumed that we have the s3 bucket already set up and also IAM rules are applied to have access to the s3 bucket.
Also we need to have ec2 instance mapped to the corresponding iam rule applied.

One thing to note that the second bat file needs to run after our first bat file is done.
So we can schedule the first bat file earlier than the second bat file and only after the first bat file is done with the backup, our second bat file will run.
```
