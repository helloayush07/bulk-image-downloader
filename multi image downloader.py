## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally





with open("sample.txt","r") as a_file:
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
            folder="hello"
            
    
    # Open a local file with wb ( write binary ) permission.
            with open("down/"+folder+"/"+filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        
                print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')
        
        
        
        
       
        





