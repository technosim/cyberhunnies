# cyberhunnies
Docker source code for a simple spinner web app. Do something nice today. Click a button creates a spinning wheel with a random selection from list of small nice gestures you can do for or with your significant other.

## See it in action
- [cyberhunnies.com](https://cyberhunnies.com)
- [spinner-webapp.azurewebsites.net](https://spinner-webapp.azurewebsites.net)

## Usage



## 1. Build the Docker Image
Navigate to the directory containing your `Dockerfile` and run:

```bash
docker build -t cyberhunnies .
```

- `-t cyberhunnies` gives your image a name.
- `.` means the build context is the current directory.

---

## 2. Verify the Image
Check that the image was created:

```bash
docker images
```

---

## 3. Run the Container
Start the container from the image:

```bash
docker run -d -p 8080:80 cyberhunnies
```

- `-d` runs it in detached mode.
- `-p 8080:80` maps port **80 inside the container** to **8080 on your host** (adjust as needed).

---

## 4. Check Logs or Status
```bash
docker ps        # See running containers
docker logs <container_id>  # View logs
```

---

##  5. Stop the Container
```bash
docker stop <container_id>
```


