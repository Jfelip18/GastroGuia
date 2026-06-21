<?php
require_once '../config.php';

// Limpiar cualquier salida anterior
if (ob_get_level()) ob_end_clean();

// Headers
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Manejar solicitud OPTIONS (preflight)
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

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
    $stmt = $pdo->prepare('DELETE FROM restaurantes WHERE id = ?');
    $stmt->execute([$id]);
    
    if ($stmt->rowCount() === 0) {
        $pdo = null;
        http_response_code(404);
        echo json_encode(['error' => 'Restaurante no encontrado'], JSON_UNESCAPED_UNICODE);
        exit;
    }
    
    $pdo = null;
    echo json_encode(['message' => 'Restaurante eliminado exitosamente'], JSON_UNESCAPED_UNICODE);
} catch (PDOException $e) {
    $pdo = null;
    http_response_code(500);
    echo json_encode(['error' => 'Error al eliminar el restaurante: ' . $e->getMessage()], JSON_UNESCAPED_UNICODE);
}