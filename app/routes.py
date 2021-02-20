import numpy as np

from flask import render_template, url_for
from app import app


review_list = [
    {
        "author":"Liz J",
        "body":"Sara, you have kept me going this last year with your fabulous Zoom classes and your sunny personality"
    },
    {
        "author":"Alicia B",
        "body":"Sara’s classes, coaching, and friendship have completely changed my life. I will never look back.",
    },
    {
        "author":"Jo H",
        "body":"Sara's classes are really something to look forward to each day: fantastic workouts; brilliant music; a lot of fun; she puts so much thought in to the variety of routines.",
    },
    {
        "author":"Andy M",
        "body":"It’s Sara’s boundless energy and infectious enthusiasm that make her classes such fun; that and the great combos is of coordination, strength, stretch and balance which all test and loosen my tight hips!!",
    },
    {
        "author":"Sue D",
        "body":"Made2Crave with Sara is physical, friendly and SO MUCH fun.",
    },
    {
        "author":"Sheila K",
        "body":"Sara, you are an inspiration! I feel fitter and full of energy as a result of your classes - you make the classes such fun that I don’t notice how hard I’m working!",
    },
    {
        "author":"Andy G",
        "body":"Sara is the Queen of online exercise classes – her enthusiasm, smiling face and professional expertise keeps me coming back for more!",
    },
    {
        "author":"Alison H",
        "body":"Sara you are an inspiration to me. Your classes are fun, varied, and certainly have the ‘feel good’ factor.",
    },
    {
        "author":"Kellie H",
        "body":"What a lovely lady to exercise with ... always full of enthusiasm, encouragement and a smile",
    },
    {
        "author":"Zoe N",
        "body":"She’s been my physical & mental life saver for the last year! Kind, thoughtful & always cheery too",
    },
    {
        "author":"Karen P",
        "body":"Sara’s classes are fantastic, they have definitely made lockdown much more bearable. I think I am much fitter and stronger than I was a year ago and am so grateful to Sara. She is always so cheerful and I feel encouraged even at 8.00am on a Monday morning.",
    },
    {
        "author":"Renee L",
        "body":"Sara's classes have helped me stay active and helped me feel connected to a fitness community- even if we are thousands of miles apart. I always get a good sweat and a huge smile. I love these classes, and Sara is the best instructor!",
    },
    {
        "author":"Ali C",
        "body":"Fun & varied classes, best thing to come out of lockdown; time just flies past",
    },
    {
        "author":"Chrissie P",
        "body":"Sara’s classes are amazing - the energy, positivity, encouragement are such a blessing and it is all down to how much she loves what she does and those she teaches.",
    },
    {
        "author":"Sarah P",
        "body":"Sara’s classes not only boost my fitness but also boost my mood! I love her positivity and her compliments always make me smile! Thanks for the injection of energy and fun into my day!",
    },
    {
        "author":"Kyle J",
        "body":"Sara is infectious with her energy, skilled with her technique, and genuinely loves all of the people in her classes. She will change your life, she certainly has mine",
    },
]
        
            

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title="Home")

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/classes/')
def classes():
    return render_template('classes.html')
        
@app.route('/personal_training/')
def personal_training():
    return render_template('personal_training.html')

@app.route('/reviews/')
def reviews():

    display_reviews = list(
        np.random.choice(
            review_list,
            np.min(
                [
                    len(review_list),
                    np.max(
                        [
                            np.random.poisson(
                                len(review_list)/3
                            ),
                            3,
                        ]
                    )
                ]
            ),
            replace=False,
        )
    )

    return render_template('reviews.html', reviews=display_reviews)

@app.route('/connect/')
def connect():
    return render_template('connect.html')
