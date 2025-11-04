<?php
// slide_stream.php
header("Content-Type: text/event-stream");
header("Cache-Control: no-cache");
header("Access-Control-Allow-Origin: *");

// Keep connection open and send updates whenever the JSON changes
$file = "current_slide.json";
$lastSent = "";

while (true) {
    clearstatcache();
    if (file_exists($file)) {
        $contents = file_get_contents($file);
        if ($contents !== $lastSent) {
            echo "data: {$contents}\n\n";
            ob_flush();
            flush();
            $lastSent = $contents;
        }
    }
    // wait briefly before checking again
    usleep(300000); // 0.3 seconds
}
?>
