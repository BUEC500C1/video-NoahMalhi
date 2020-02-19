from PIL import Image, ImageDraw

def convert_text(tweet_texts):
    iter = 0
    #for tweet in tweet_texts:
    for x in tweet_texts:
        
        filename = "img0" + str(iter) + ".png"
        f = open(filename, "w+")
        image = Image.new(mode = "RGB", size = (200,70), color = "red")
        draw = ImageDraw.Draw(image)
        draw.text((10,10), x , fill=(255,255,0))
        image.save(filename)
        iter +=1
        filename = ''
        f.close()
   
  

