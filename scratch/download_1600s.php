<?php
$urls = [
    'lucci-bts-shoot' => 'https://static.showit.co/1600/JnajaFlpVMGJZAZJh8qJsA/292551/photo_dec_13_2025_3_46_00_pm.jpg',
    'lucci-bts-table' => 'https://static.showit.co/1600/0wzOBg_6ZGUcbrb8ABtjxA/292551/photo_apr_01_2026_12_45_51_pm.jpg',
    'lucci-bts-studio' => 'https://static.showit.co/1600/9d2XotlfzbhoQ1H7NSTsZg/292551/img_9039.jpg'
];
$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0\r\n"]];
$ctx = stream_context_create($opts);

foreach ($urls as $name => $url) {
    $dest = "c:/xampp/htdocs/luci/assets/lucci/{$name}.jpg";
    $d = @file_get_contents($url, false, $ctx);
    if ($d) {
        file_put_contents($dest, $d);
        echo "Saved {$dest} (" . strlen($d) . " bytes)\n";
    }
}

