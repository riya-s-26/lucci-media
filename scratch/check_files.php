<?php
$files = [
    'lucci-wide-1' => 'c:/xampp/htdocs/luci/assets/lucci/lucci-wide-1.jpg',
    'lucci-wide-2' => 'c:/xampp/htdocs/luci/assets/lucci/lucci-wide-2.jpg',
    'lucci-wide-3' => 'c:/xampp/htdocs/luci/assets/lucci/lucci-wide-3.jpg',
    'lucci-wide-4' => 'c:/xampp/htdocs/luci/assets/lucci/lucci-wide-4.jpg',
    'lex-camera-onset' => 'c:/xampp/htdocs/luci/assets/lucci/lex-camera-onset.jpg',
    'hero-bg' => 'c:/xampp/htdocs/luci/assets/hero-bg.jpg',
];

foreach ($files as $name => $path) {
    if (file_exists($path)) {
        echo "$name exists, size: " . filesize($path) . " bytes\n";
    }
}

