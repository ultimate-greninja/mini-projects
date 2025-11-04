<?php
session_start();
if (empty($_SESSION['is_host'])) {
  http_response_code(403);
  echo "Forbidden";
  exit;
}

$data = json_decode(file_get_contents("php://input"), true);
$file = 'current_slide.json';
$current = [];
if (file_exists($file)) {
  $current = json_decode(file_get_contents($file), true) ?: [];
}

$changed = false;
if (!empty($data['slide'])) {
  $current['slide'] = $data['slide'];
  $changed = true;
}
if (array_key_exists('message', $data)) {
  // allow empty string to clear
  $current['message'] = $data['message'];
  $changed = true;
}

if ($changed) {
  file_put_contents($file, json_encode($current));
  echo "ok";
} else {
  echo "no-change";
}
