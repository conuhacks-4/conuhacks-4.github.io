
<html>
    <head>
        <title> Our Website </title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        

        <style>
            h1, h2, h3 {
            font-family: sans-serif;
            font-size: 30px;
            font-weight: 400;
            text-transform: uppercase;
            }

            body {
                font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
                font-size: 16px;
                line-height: 1.5;
                margin: 0;
                background: #2a2a2a;
            }

            .outer {
                width: 80%;
                margin: auto;
                background: #fcfcfc;
                padding-top: 25px;
            }

            .inner {
                width: 100%;
                margin: auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 210px;
                grid-gap: 24px 24px;
                padding-top: 25px;
            }

            .header {
                font-size: 80px;
                text-align: center;
                grid-column: 1/span 2;
                background-image: url("static/concert.jpg");
                font-family: sans-serif;
                font-weight: 900;
                text-transform: uppercase;
                text-transform: uppercase;
                background-position: 0px 290px;
                background-size: cover;
            }

            .subheader {
                font-size: 32px;
                font-weight: 400;
            }

            #myDiv1 {
                grid-column: 1;
            }

            .trend {
                grid-column: 1/span 2;
                text-align: center;
                margin: 5px 50px;
                background-color: #ccccff;
                padding: 20px;
            }

            #myDiv2 {
                grid-column: 2;
            }

            #myDiv3 {
                grid-column: 1/ span 2;
            }

            #VH {
                grid-column: 1;
            }

            .trend2 {
                grid-column: 2;
                padding: 50px;
            }

            #Avicii{
                grid-column: 1/span 2;
            }

            .graph3 {
                grid-column: 1;
            }

            #Aretha {
                grid-column: 2;
            }

            #Aretha2 {
                grid-column: 1;
            }

            .head {
                font-family: sans-serif;
                font-size: 30px;
                font-weight: 400;
                text-transform: uppercase;
                padding-left: 30px;
            }

            .head2 {
                font-family: sans-serif;
                font-size: 30px;
                font-weight: 400;
                text-transform: uppercase;
                text-align: center;
                grid-column: 1/span 2;
            }

            
        

        </style>


    </head>


    <body>
        <div class="header"> 
            TouchTunes 
        <div class="subheader">
            Analysing trends of 2018
        </div>
        </div>

        <div id="VH"><!-- Van Halen --></div> 
        <div class="trend2"> <h3> Control Data</h3>
            As we can see, Van Halen being a considerably popular rock band and having easy "go to" songs at any time of the year, they appear to have a particularly constant trend of being played in bars and places of the sort. Their songs are classics of the past and will remain so for years to come, so they won't tend to have any drastic changes unless they get affected by the popular media, as we will see for these next trends.
        </div>

        <div class="head"> Movies </div>
        <div id="myDiv1"><!-- Plotly chart will be drawn inside this DIV --></div>
        <div id="myDiv2"><!-- Plotly chart will be drawn inside this DIV --></div>   

        <div id="myDiv3"><!-- Bohemian --></div>   

        <div class="trend"> 
        The release of the movie "Bohemian Rhapsody", on octorber 24th 2018, clearly caused an incredible peak in the number of times people would play Queen's songs. This comes as no suprise as the band had probably the best form of media to spark nostalgia to the old fans and intrest in new fans. Add this with the fact that they are already substancially more popular than most rock bands, and you end up with a graph like this.
        </div>
        

        <div class="head2"> Trends caused by the death of a singer </div>

        <div id="Avicii"><!-- Avicii --></div> 
        <div class= "trend">We wanted to see if there were any trends that would appear due to the death of certain signers, and sure enough there were. Avicii died April 20th 2018 and on the graph we can see a rise in the number of plays around this time of the year. </div>
        
        <div id="Aretha2"></div>
        <div id="Aretha"><!-- Aretha --></div> 
        
        
        <div class="trend"> 
        This graph is particularly interesting because you can see that a singer can go completely unnoticed until something drastic happens. When Aretha Franklin died on august 16th 2018, you can clearly see people have chosen to play her songs almost 4 times as much as before. This is a comprehensible movement that went towards paying respects to the singer by playing her songs. The peak must have also been caused by the high media coverage that drew people to listen to her music when they normally wouldn't.
        </div>


        <script src="grapher.js"></script>
        
    </body>

</html>