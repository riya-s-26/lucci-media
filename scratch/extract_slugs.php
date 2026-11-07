<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa_about.html');
$slugs = ['founder-banner', 'view-1', 'view-2', 'view-3', 'team-banner'];
foreach ($slugs as $s) {
    echo "=== SLUG: $s ===\n";
    $pos = strpos($html, 'id="' . $s . '"');
    if ($pos !== false) {
        echo substr($html, $pos, 1500) . "\n--------------------------------\n";
    }
}

