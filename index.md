
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
                grid-template-columns: 1fr 1fr 1fr;
                grid-gap: 24px 24px;
                padding-top: 25px;
            }

            .header {
                font-size: 80px;
                text-align: center;
                grid-column: 1/span 3;
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
                grid-column: 1/span 2;
                margin-top: 30px;
                margin-bottom: 30px;
            }

            .trend {
                grid-column: 3;
            }

            #myDiv2 {
                grid-column: 1/span 2;
                margin-top: 30px;
                margin-bottom: 30px;
            }

            .graph3 {
                grid-column: 3;
                margin-top: 30px;
                margin-bottom: 30px;
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

        <div id="myDiv1"><!-- Plotly chart will be drawn inside this DIV --></div>

        <div class="trend"> trend </div>

        <div id="myDiv2"><!-- Plotly chart will be drawn inside this DIV --></div>    

        <div class="trend"> trend </div>

        <div class="graph3">
            graph3
        </div>

        <script src="grapher.js"></script>
        
    </body>

</html>