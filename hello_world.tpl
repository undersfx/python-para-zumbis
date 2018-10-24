<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
	<title>Python para Zumbis</title>
</head>
<body>
	<p>
		Bem Vindo {{username}}
	</p>
	
	<ul>
	%for thing in things:
		<li>{{thing}}</li>
		%end
	</ul>
	
	<p>
		<form action="/favorita" method="POST">
			Qual sua linguagem favorita ?
			<input type="text" name="lang" size="40" value=""><br>
			<input type="submit" value="Submit">
		</form>
	</p>
</body>
</html>