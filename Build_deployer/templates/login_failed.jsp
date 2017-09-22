<!-- Build_deployer/templates/login_failed.jsp -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Login form using HTML5 and CSS3</title>
<link rel="stylesheet" href="/static/css/style.css">
</head>

<body>
<body>
	<div class="container">
		<section id="content">
			<form action="/build/" method="post">
				<h1>Build Deployer</h1>
				{% csrf_token %}
    			{{ login_form }}
				<h4>Authentication failed</h4>
				<input type="submit" value="Log in" />

					<!-- <a href="#">Lost your password?</a>
				<a href="#">Register</a> -->
			</form>
			<!-- form -->
			<!--<div class="button">
			<a href="#">Download source file</a>
		</div>-->
			<!-- button -->
		</section>
		<!-- content -->
	</div>
	<!-- container -->
</body>

<!-- <script src="/static/js/index.js"></script>-->

</body>
</html>