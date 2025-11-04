<?php session_start(); ?>
<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <script>
    (function() {
      try {
        document.addEventListener('DOMContentLoaded', function() {
          var metas = document.querySelectorAll('meta[name="viewport"]');
          metas.forEach(function(m) {
            if (/target-densitydpi/i.test(m.content || '')) {
              m.parentNode.removeChild(m);
              console && console.log && console.log('Removed obsolete viewport meta with target-densitydpi');
            }
          });
        });
      } catch (e) {}
    })();
  </script>
  <title>Host chooser</title>
</head>

<body style="font-family:Arial;padding:2rem">
  <h1>Choose: Host or Viewer</h1>

  <!-- Error message if wrong host code -->
  <?php
  if (isset($_SESSION['error'])) {
    echo "<p style='color:red'>" . htmlspecialchars($_SESSION['error']) . "</p>";
    unset($_SESSION['error']); // clear message after showing
  }
  ?>

  <form method="post" action="check.php">
    <label><input type="radio" name="mode" value="viewer" checked> Viewer</label>
    <label style="margin-left:1rem"><input type="radio" name="mode" value="host"> Host</label>

    <div style="margin-top:1rem">
      <input type="text" name="code" placeholder="Host code (if Host)" />
    </div>

    <div style="margin-top:1rem">
      <button type="submit">Proceed</button>
    </div>
  </form>
</body>

</html>