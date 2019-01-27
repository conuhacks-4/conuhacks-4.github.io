
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

            .background {
                background-image: linear-gradient(white, transparent 70%), url('');
                background-size: 100% 100%;
                background-position: 0% 0%;
                background-blend-mode: screen; /* so many of them */

                position: absolute;
                width: 100%;
                height: 200px;
                left: 0;
                bottom: 0;
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
            }

            #Avicii{
                grid-column:  1;
            }

            .graph3 {
                grid-column: 1;
            }
        

        </style>


    </head>


    <body>
        <div class="header"> 
            TouchTunes 
        <div class="subheader">
        Bohemian Rhapsody Trends
        </div>
        </div>

        <div id="VH"><!-- Van Halen --></div> 
        <div class="trend2"> <h3> Control Data</h3>
            <p>As we can see, Van Halen being a considerably popular rock band and having easy "go to" songs at any time of the year, they appear to have a particularly constant trend of being played in bars and places of the sort. Their songs are classics of the past and will remain so for years to come, so they won't tend to have any drastic changes unless they get affected by the popular media, as we will see for these next trends.</p>
        </div>

        <h4> Movies </h4>
        <div id="myDiv1"><!-- Plotly chart will be drawn inside this DIV --></div>
        <div id="myDiv2"><!-- Plotly chart will be drawn inside this DIV --></div>   

        <div id="myDiv3"><!-- Bohemian --></div>   

        <div class="trend"> 
        <p>The release of the movie "Bohemian Rhapsody" clearly caused an incredible peak in the number of times people would play Queen's songs. This comes as no suprise as the band had probably the best form of media to spark nostalgia to the old fans and intrest in new fans. Add this with the fact that they are already substancially more popular than most rock bands, and you end up with a graph like this.</p>
        </div>
        

        <div id="Avicii"><!-- Avicii --></div> 

        <div class= "trend2">trend</div>

        <div id="Aretha"><!-- Aretha --></div> 

        <script src="grapher.js"></script>
        
    </body>

</html>