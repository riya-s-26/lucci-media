<?php
$url = 'https://luccimedia.com/';
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
$html = curl_exec($ch);
curl_close($ch);

if (!$html) {
    echo "Failed to fetch\n";
    exit;
}

echo "Fetched HTML, length: " . strlen($html) . "\n";

// Find all CSS stylesheets
preg_match_all('/<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']/i', $html, $css);
echo "\nStylesheets:\n";
print_r($css[1]);

// Find all Scripts
preg_match_all('/<script[^>]+src=["\']([^"\']+)["\']/i', $html, $scripts);
echo "\nScripts:\n";
print_r($scripts[1]);

// Search for animation-related keywords in html
preg_match_all('/(data-scroll[^\s>]*|data-aos[^\s>]*|data-reveal[^\s>]*|data-parallax[^\s>]*|class="[^"]*(?:reveal|parallax|scroll|fade|curtain|zoom|scale)[^"]*")/i', $html, $anims);
echo "\nAnimation Attributes / Classes:\n";
print_r(array_unique($anims[0]));

