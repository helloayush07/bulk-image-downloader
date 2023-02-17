## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import os



with open("sample.txt", "r") as file:
    
    data = file.readlines()
    for line in data:
        fileurl = open('url.txt', 'w')
        word = line.split()
        
        print(word[0])
        par_path="C:/Users/KIIT/Desktop/bulk image downloder/down"
        path=os.path.join(par_path,word[0])
        os.makedirs(path)
        folder="down/"+word[0]
        for sr in range(1,len(word)):
            fileurl.write(word[sr]+"\n")
            
        
        with open("url.txt","r") as a_file:
            for line in a_file:
                sline=line.strip()
                print(sline)


                image_url = sline
                filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
                r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
                if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                    r.raw.decode_content = True

            
            
    
    # Open a local file with wb ( write binary ) permission.
                    with open(folder+"/"+filename,'wb') as f:
                        shutil.copyfileobj(r.raw, f)

            
        
               
                else:   
                    print('Image Couldn\'t be retreived')
        
fileurl.close()
a_file.close()
        
        
       
        




