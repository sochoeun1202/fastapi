# FastAPI Docker Management Script
# Usage: ./docker-manage.ps1 [command]

param(
    [Parameter(Mandatory=$false)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "FastAPI Docker Management Script" -ForegroundColor Green
    Write-Host "=================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Available commands:" -ForegroundColor Yellow
    Write-Host "  help     - Show this help message"
    Write-Host "  build    - Build the Docker image"
    Write-Host "  up       - Start all services (development)"
    Write-Host "  down     - Stop all services"
    Write-Host "  restart  - Restart all services"
    Write-Host "  logs     - Show logs from all services"
    Write-Host "  status   - Show status of all services"
    Write-Host "  clean    - Clean up containers and images"
    Write-Host "  db       - Access MySQL database"
    Write-Host "  shell    - Access FastAPI container shell"
    Write-Host "  test     - Run tests in container"
    Write-Host ""
    Write-Host "Production commands:" -ForegroundColor Cyan
    Write-Host "  prod-up  - Start production environment"
    Write-Host "  prod-down - Stop production environment"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Magenta
    Write-Host "  ./docker-manage.ps1 build"
    Write-Host "  ./docker-manage.ps1 up"
    Write-Host "  ./docker-manage.ps1 logs"
}

function Build-Image {
    Write-Host "Building Docker image..." -ForegroundColor Green
    docker-compose build --no-cache
}

function Start-Services {
    Write-Host "Starting services..." -ForegroundColor Green
    docker-compose up -d
    Write-Host "Services started. Access points:" -ForegroundColor Yellow
    Write-Host "  - FastAPI: http://localhost:8000" -ForegroundColor White
    Write-Host "  - API Docs: http://localhost:8000/docs" -ForegroundColor White
    Write-Host "  - phpMyAdmin: http://localhost:8080" -ForegroundColor White
}

function Stop-Services {
    Write-Host "Stopping services..." -ForegroundColor Green
    docker-compose down
}

function Restart-Services {
    Write-Host "Restarting services..." -ForegroundColor Green
    docker-compose restart
}

function Show-Logs {
    Write-Host "Showing logs..." -ForegroundColor Green
    docker-compose logs -f
}

function Show-Status {
    Write-Host "Service status:" -ForegroundColor Green
    docker-compose ps
}

function Clean-Docker {
    Write-Host "Cleaning up Docker resources..." -ForegroundColor Yellow
    Write-Host "This will remove all containers, images, and volumes!" -ForegroundColor Red
    $confirm = Read-Host "Are you sure? (y/N)"
    if ($confirm -eq "y" -or $confirm -eq "Y") {
        docker-compose down -v --rmi all
        docker system prune -f
        Write-Host "Cleanup completed." -ForegroundColor Green
    } else {
        Write-Host "Cleanup cancelled." -ForegroundColor Yellow
    }
}

function Access-Database {
    Write-Host "Accessing MySQL database..." -ForegroundColor Green
    docker-compose exec mysql mysql -u dev -pdev123! testdb
}

function Access-Shell {
    Write-Host "Accessing FastAPI container shell..." -ForegroundColor Green
    docker-compose exec web bash
}

function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Green
    docker-compose exec web python test_connection.py
}

function Start-Production {
    Write-Host "Starting production environment..." -ForegroundColor Green
    docker-compose -f docker-compose.prod.yml up -d
}

function Stop-Production {
    Write-Host "Stopping production environment..." -ForegroundColor Green
    docker-compose -f docker-compose.prod.yml down
}

# Main script logic
switch ($Command.ToLower()) {
    "help" { Show-Help }
    "build" { Build-Image }
    "up" { Start-Services }
    "down" { Stop-Services }
    "restart" { Restart-Services }
    "logs" { Show-Logs }
    "status" { Show-Status }
    "clean" { Clean-Docker }
    "db" { Access-Database }
    "shell" { Access-Shell }
    "test" { Run-Tests }
    "prod-up" { Start-Production }
    "prod-down" { Stop-Production }
    default { 
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Write-Host ""
        Show-Help
    }
}
