
#Set the runtime language and version
FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specificed packages
RUN pip install -r requirements.txt

# Copy all files in ./app
COPY app/* ${LAMBDA_TASK_ROOT}

#Set the CMD to your handler (also possible as a parameter override outside of the Dockerfile)
CMD [ "main.header" ]