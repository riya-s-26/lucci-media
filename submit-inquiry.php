<?php
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method Not Allowed']);
    exit;
}

// Read input
$input = $_POST;
if (empty($input)) {
    $raw = file_get_contents('php://input');
    if (!empty($raw)) {
        $input = json_decode($raw, true) ?? [];
    }
}

// Validate primary required fields
$name = trim($input['name'] ?? '');
$brand = trim($input['brand_name'] ?? '');

if (empty($name) || empty($brand)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'error' => 'Please fill in all required fields.']);
    exit;
}

$logEntry = [
    'timestamp'        => date('c'),
    'name'             => $name,
    'brand_name'       => $brand,
    'website_handle'   => trim($input['website_handle'] ?? ''),
    'location'         => trim($input['location'] ?? ''),
    'brand_type'       => trim($input['brand_type'] ?? ''),
    'interest'         => trim($input['interest'] ?? ''),
    'monthly_revenue'  => trim($input['monthly_revenue'] ?? ''),
    'marketing_budget' => trim($input['marketing_budget'] ?? ''),
    'start_date'       => trim($input['start_date'] ?? ''),
    'success_vision'   => trim($input['success_vision'] ?? ''),
    'referral_source'  => trim($input['referral_source'] ?? ''),
    'user_agent'       => $_SERVER['HTTP_USER_AGENT'] ?? 'unknown',
    'ip'               => $_SERVER['REMOTE_ADDR'] ?? 'unknown'
];

$logFile = __DIR__ . '/inquiries_log.json';
$existing = [];
if (file_exists($logFile)) {
    $existing = json_decode(file_get_contents($logFile), true) ?: [];
}
$existing[] = $logEntry;
@file_put_contents($logFile, json_encode($existing, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));

echo json_encode([
    'success' => true,
    'message' => 'Received. We will be in touch soon.'
]);
