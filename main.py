import uvicorn

if __name__ == "__main__":      
    uvicorn.run("app.app:app", host="[IP_ADDRESS]",reload= True,port=8000)
