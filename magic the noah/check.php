<?php
session_start();

$mode = $_POST['mode'] ?? 'viewer';
$code = $_POST['code'] ?? '';

// If the user picked Viewer, go straight to viewer.php
if ($mode === 'viewer') {
    header('Location: viewer.php');
    exit;
}

// If Host was chosen, validate the host code
if ($code === 'e621') {
    $_SESSION['is_host'] = true; // store the host flag
    header('Location: host.php');
    exit;
} else {
    // wrong code — send back with error message
    $_SESSION['error'] = 'Wrong code';
    header('Location: index.php');
    exit;
}
?>
