<!-- Build_deployer/templates/index.jsp -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Build deployment</title>
<link rel="stylesheet" href="/static/css/style.css">
</head>

<body>
<body>
	<div class="container">
		<section id="content">
			<form action="/build/login.jsp" method="post">
				<h1>Build deployment</h1>
			<!-- <input type="text" placeholder="Username" required="" id="username" />
				<input type="password" placeholder="Password" required="" id="password" /> -->
				{% csrf_token %}
    			{{ login_form }}
    			<h4 {{login_fail}}>Authentication failed</h4>
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