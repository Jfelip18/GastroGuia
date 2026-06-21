<?php
require_once '../config.php';

// Limpiar cualquier salida anterior
if (ob_get_level()) ob_end_clean();

// Headers
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

$id = isset($_GET['id']) ? $_GET['id'] : null;

if (!$id) {
    http_response_code(400);
    echo json_encode(['error' => 'ID no proporcionado'], JSON_UNESCAPED_UNICODE);
    exit;
}

$pdo = getDBConnection();

if (!$pdo) {
    http_response_code(500);
    echo json_encode(['error' => 'Error de conexión a la base de datos']);
    exit;
}

try {
    $stmt = $pdo->prepare('SELECT * FROM restaurantes WHERE id = ?');
    $stmt->execute([$id]);
    $restaurant = $stmt->fetch(PDO::FETCH_ASSOC);
    
    $pdo = null;
    
    if (!$restaurant) {
        http_response_code(404);
        echo json_encode(['error' => 'Restaurante no encontrado'], JSON_UNESCAPED_UNICODE);
        exit;
    }
    
    echo json_encode($restaurant, JSON_UNESCAPED_UNICODE);
} catch (PDOException $e) {
    $pdo = null;
    http_response_code(500);
    echo json_encode(['error' => 'Error al obtener el restaurante: ' . $e->getMessage()], JSON_UNESCAPED_UNICODE);
}