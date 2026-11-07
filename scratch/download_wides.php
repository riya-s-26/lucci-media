<?php
$imgs = [
    'lucci-wide-1' => 'https://static.showit.co/1200/ohQSnJzQWLpHx1PLrkyXig/292551/photo-2026-04-08-14-48-56.jpg',
    'lucci-wide-2' => 'https://static.showit.co/1200/ms4WgKQKAEN8W5MZTW_LrQ/292551/photo_dec_13_2025_2_36_15_pm.jpg',
    'lucci-wide-3' => 'https://static.showit.co/1200/JnajaFlpVMGJZAZJh8qJsA/292551/photo_dec_13_2025_3_46_00_pm.jpg',
    'lucci-wide-4' => 'https://static.showit.co/1200/0wzOBg_6ZGUcbrb8ABtjxA/292551/photo_apr_01_2026_12_45_51_pm.jpg',
];

$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0\r\n"]];
$ctx = stream_context_create($opts);

foreach ($imgs as $name => $url) {
    $dest = "c:/xampp/htdocs/luci/assets/lucci/{$name}.jpg";
    $data = @file_get_contents($url, false, $ctx);
    if ($data) {
        file_put_contents($dest, $data);
        echo "Saved {$dest} (" . strlen($data) . " bytes)\n";
    }
}

