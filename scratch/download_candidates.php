<?php
$imgs = [
    'photo_dec_13_2025_2_36_15_pm' => 'https://static.showit.co/1200/ms4WgKQKAEN8W5MZTW_LrQ/292551/photo_dec_13_2025_2_36_15_pm.jpg',
    'photo_dec_13_2025_3_46_00_pm' => 'https://static.showit.co/1200/JnajaFlpVMGJZAZJh8qJsA/292551/photo_dec_13_2025_3_46_00_pm.jpg',
];

$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0\r\n"]];
$ctx = stream_context_create($opts);

foreach ($imgs as $name => $url) {
    $dest = "c:/xampp/htdocs/luci/assets/lucci/{$name}.jpg";
    echo "Downloading {$name}...\n";
    $data = @file_get_contents($url, false, $ctx);
    if ($data) {
        file_put_contents($dest, $data);
        echo "Saved {$dest} (" . strlen($data) . " bytes)\n";
    } else {
        echo "Failed to download {$name}\n";
    }
}

