# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install numpy pandas scikit-learn wandb jupyter

# Command to run Jupyter Notebook inside the container
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
 
