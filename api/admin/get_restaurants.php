<?php
require_once '../config.php';

// Limpiar cualquier salida anterior
if (ob_get_level()) ob_end_clean();

// Headers
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

$pdo = getDBConnection();

if (!$pdo) {
    http_response_code(500);
    echo json_encode(['error' => 'Error de conexión a la base de datos']);
    exit;
}

try {
    $query = 'SELECT id, nombre, descripcion, direccion, zona_r, tipo, precio_min, precio_max, plato_economico, plato_caro, url, calificacion, caracteristicas FROM restaurantes ORDER BY nombre';
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    $restaurants = $stmt->fetchAll();
    
    // Cerrar la conexión explícitamente
    $stmt = null;
    $pdo = null;
    
    echo json_encode($restaurants, JSON_UNESCAPED_UNICODE);
    
} catch (PDOException $e) {
    // Cerrar conexión en caso de error
    $pdo = null;
    
    http_response_code(500);
    echo json_encode([
        'error' => 'Error al obtener los restaurantes',
        'message' => $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);
}
?>