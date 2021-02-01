# paid-promotions-delete

## Ad-blocker for those sneaky in - video  paid promotions in online streaming platforms.






## Tasks
1. <del>Speech recognition up and running </del>
2. <del>Test with audio files</del>
3. Read from a video file test
4. Save time markers for bounds of promotion 
5. <del>Compile List of keywords to search for ("Discount", "Coupon Code", "Our friends at so and so.."</del>
6. <del>Turn .txt list of keywords to python list </del>
7. Pull video down from streaming site 
8. Cropping part of a video out .( native fast forward from streaming service maybe?)
9. Make a traditional ad blocker 
10. <del>Test Duration and Noise in recognition</del>
11. Find which api that will do longer samples(google is cutting off the sample)
12. Look for repititions of words in the sample
13. <del>Count occurances of of words in samples</del>



## Getting started 

Installing the Speech Recognition wrapper
`pip install SpeechRecognition `



Needed to convert some sample mp3 to wav
`ffmpeg -i input.mp3 output.wav `


## Usage
Use txt_to_list.py takes in a txt based list of phrases and keywords and outputs a list of those terms.  Phrases are left whole and split into single words to be compared against.

With recognize.py, output is a set of matched terms from the comparison of a promotional sample and the list of keywords and phrases.

Audio Sample:

```["today's", 'sponsor', 'raid', 'Shadow', 'Legend', 'and', 'play', 'this', 'game', 'all', 'the', 'time', 'and', 'there', 'was', 'a', 'huge', 'supporter', 'of', 'this', 'channel', 'description', 'below']
```

Matched Keywords against a list of common marketing phrases, buzz words, and youtube slang:

```{'this', 'channel', 'a', 'huge', 'and', 'description', 'the', 'of', 'supporter', 'below'}```




Repitition of words could indicate a segment of video being a paid promotion. The following are a few well known big budget commercials:

```['apply', 'directly', 'to', 'the', 'forehead', 'head', 'on', 'directly', 'to', 'the', 'forehead', 'head', 'on', 'Walgreens']
{'to', 'the'}
{'apply': 1, 'directly': 2, 'to': 2, 'the': 2, 'forehead': 2, 'head': 2, 'on': 2, 'Walgreens': 1}
```

and this is an easy one to guess...

```meow.wav
['meow', 'meow', 'meow', 'meow', 'meow', 'meow', 'meow', 'meow', 'meow', 'meow', 'meow']
set()
{'meow': 11}
```

Using  `rec.recognize_google(audio, show_all=True)` You can get all the possible translations :


```{'alternative': [{'transcript': "who was made with real bacon there's no time "
                                'like Beggin'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like begging'},
                 {'transcript': 'who was made with real bacon there is no time '
                                'like begging'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like baygon'},
                 {'transcript': 'who was made with real bacon is no time like '
                                'begging'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like bagin'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like baking'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like bacon'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like bekon'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like beacon'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like bega'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like benning'},
                 {'transcript': "who was made with real bacon there's no time "
                                'like beken'}],
```




## Ideas
- Get rid of the comments section also
- As a chrome extension , Pre-scan/listn to  video , re-direct 
- List of approved content producers that don't have spam in their videos 
- Get rid of ad spam on legitmate news sources 
- Machine learning to determine if content is Paid sponsorship or not

# Credits / Resources 
https://realpython.com/python-speech-recognition/
https://www.honeycopy.com/copywritingblog/powerful-marketing-words
https://ontiva.com/en

