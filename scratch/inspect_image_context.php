<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/luccimedia.html');
$keys = [
    'photo-2026-04-08-14-48-56',
    'photo_dec_13_2025_2_36_15_pm',
    'photo_dec_13_2025_3_46_00_pm',
    'photo_apr_01_2026_12_45_51_pm'
];

foreach ($keys as $k) {
    $pos = strpos($html, $k);
    if ($pos !== false) {
        echo "=== $k ===\n";
        echo substr($html, max(0, $pos - 150), 300) . "\n";
    }
}

