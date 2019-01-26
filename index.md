<DOCTYPE !>
<html>
    <head>
        <title> Our Website </title>
    </head>

    <body>
        <div> Hello </div>
        <script> 
            var text = '{"employees":[' +
            '{"firstName":"John","lastName":"Doe" },' +
            '{"firstName":"Anna","lastName":"Smith" },' +
            '{"firstName":"Peter","lastName":"Jones" }]}';

            obj = JSON.parse(text);
            document.getElementById("demo").innerHTML =
            obj.employees[1].firstName + " " + obj.employees[1].lastName;
        </script>

    </body>

</hmtl>