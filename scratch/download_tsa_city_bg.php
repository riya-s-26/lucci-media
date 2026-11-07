<?php
$url = 'https://static.showit.co/1600/5ay0cmJVgsWNJg5N0Ak5Nw/204040/untitled_design.jpg';
$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0\r\n"]];
$ctx = stream_context_create($opts);
$dest = 'c:/xampp/htdocs/luci/assets/lucci/tsa-city-bg.jpg';
$d = @file_get_contents($url, false, $ctx);
if ($d) {
    file_put_contents($dest, $d);
    echo "Saved {$dest} (" . strlen($d) . " bytes)\n";
} else {
    echo "Failed to download\n";
}

