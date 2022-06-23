<!-- Poolball GMs Homepage -->

<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>

    <meta charset="utf-8">
    <link rel="stylesheet" href="index.css">
    <link rel="stylesheet" href="navbar.css">

    <title>Poolball GMs</title>

    <!-- favicon -->
    <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">
    <link rel="manifest" href="images/site.webmanifest">

</head>

<!-- HTML site body -->

    <body>

    <header>
        <a href="#"><img src="images/logo.png" alt="logo" class="logo"></a>
        
        <nav>
          <ul>
            <li><a href="news.html">News</a></li>
            <li><a href="teams.html">Teams</a></li>
            <li><a href="season.html">Season</a></li>
            <li><a href="games.html">Games</a></li>
            <li><a href="prospects.html">Prospects</a></li>
          </ul>
        </nav>

    </header>

    <table class="layout" width="100%">

        <tr> 
            <td align="center"> <img src="images/logo.svg" alt="poolball" class="ball"> </td> 
        </tr>

        <tr>
            <td align="center"><button class="button" onclick="document.getElementById('pop1').style.display='block'">Manager Login</button></td>
        </tr>

    </table>


    <!-- Login Popup -->
    <div id="pop1" class="popup animate">
        <center><form class="login" action="manager.php" method="POST">
                <h1>Poolball Manager Login</h1>
                <span class="close" title="Close Login" onclick="document.getElementById('pop1').style.display='none'">&times;</span>
                <label for="uname">Username</label>
                <input type="text" placeholder="Enter Username" name="uname" required>
    
                <label for="psw">Password</label>
                <input type="password" placeholder="Enter Password" name="psw" required>
    
                <button type="submit" class="submitbtn">Login</button>
        </form></center>
    </div>


    <!-- Footer -->
    <footer>
        <ul>
            <li><a href="https://discord.com/channels/872517520341467146/872518021057495140">
                <img src="images/discord-logo-white.svg" class="media">
            </a></li>

            <li><a href="https://github.com/ItsMeToast/PoolballGMsPublic">
                <img src="images/github-logo-white.png" class="media">
            </a></li>
          </ul>
    </footer>

    </body>

</html>
