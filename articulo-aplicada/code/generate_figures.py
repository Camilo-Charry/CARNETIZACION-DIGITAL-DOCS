#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Gráficas para Plantilla LaTeX - Sistemas de Control de Acceso con QR y RFID
Genera gráficas relacionadas con tecnologías de identificación digital, eficiencia operativa y métricas de adopción
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
import os

# Configuración global para mejorar la calidad de las gráficas
plt.style.use('default')
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 9
rcParams['figure.titlesize'] = 13
rcParams['savefig.dpi'] = 300
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.pad_inches'] = 0.1

# Crear directorio de gráficas si no existe
graphics_dir = 'graphics'
os.makedirs(graphics_dir, exist_ok=True)

def generar_eficiencia_acceso():
    """Genera gráfica de barras comparando tiempos de acceso con diferentes métodos"""

    # Datos de ejemplo: tiempos de acceso en segundos
    metodos = ['Manual\n(Papel)', 'Tarjeta\nRFID', 'Código\nQR', 'Biométrico']
    tiempos_acceso = [45.2, 2.1, 3.8, 1.5]  # segundos promedio
    precision = [85, 98, 95, 99]  # porcentaje de precisión

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfica 1: Tiempo de Acceso
    bars1 = ax1.bar(metodos, tiempos_acceso, color=['#C73E1D', '#F18F01', '#2E86AB', '#A23B72'])
    ax1.set_title('Tiempo Promedio de Acceso')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_ylim(0, 50)

    # Añadir valores en las barras
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}s', ha='center', va='bottom')

    # Gráfica 2: Precisión de Identificación
    bars2 = ax2.bar(metodos, precision, color=['#C73E1D', '#F18F01', '#2E86AB', '#A23B72'])
    ax2.set_title('Precisión de Identificación')
    ax2.set_ylabel('Precisión (%)')
    ax2.set_ylim(0, 100)

    # Añadir valores en las barras
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.0f}%', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/eficiencia_acceso.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/eficiencia_acceso.png', format='png')
    plt.close()
    print("✓ Generada: eficiencia_acceso.pdf/png")

def generar_adopcion_tecnologias():
    """Genera gráfica de líneas mostrando adopción de tecnologías QR/RFID"""

    # Datos de ejemplo: adopción mensual
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
    adopcion_qr = [15, 22, 28, 35, 42, 48, 55, 62, 68, 74, 79, 83]
    adopcion_rfid = [8, 12, 18, 25, 32, 38, 45, 52, 58, 65, 71, 76]
    usuarios_totales = [1200, 1250, 1320, 1380, 1450, 1520, 1580, 1650, 1720, 1780, 1850, 1900]

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Eje Y izquierdo: Adopción de tecnologías
    color = '#2E86AB'
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Adopción Tecnológica (%)', color=color)
    line1 = ax1.plot(meses, adopcion_qr, color=color, marker='o', linewidth=2,
                     label='Adopción Código QR (%)')
    line2 = ax1.plot(meses, adopcion_rfid, color='#F18F01', marker='s', linewidth=2,
                     label='Adopción RFID (%)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 100)

    # Eje Y derecho: Usuarios totales
    ax2 = ax1.twinx()
    color = '#C73E1D'
    ax2.set_ylabel('Usuarios Registrados', color=color)
    line3 = ax2.plot(meses, usuarios_totales, color=color, marker='^', linewidth=2,
                     label='Usuarios Totales')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(1000, 2000)

    # Leyenda combinada
    lines = line1 + line2 + line3
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='center right')

    plt.title('Adopción de Tecnologías de Identificación Digital (2024)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/adopcion_tecnologias.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/adopcion_tecnologias.png', format='png')
    plt.close()
    print("✓ Generada: adopcion_tecnologias.pdf/png")

def generar_correlacion_tecnologias():
    """Genera gráfica de dispersión mostrando correlación entre adopción tecnológica y eficiencia"""

    np.random.seed(42)  # Para reproducibilidad

    # Datos simulados: correlación entre adopción tecnológica y reducción de tiempo
    n_instituciones = 30
    adopcion_tecnologica = np.random.normal(65, 20, n_instituciones)
    adopcion_tecnologica = np.clip(adopcion_tecnologica, 10, 95)

    # Correlación positiva con algo de ruido
    reduccion_tiempo = 0.7 * adopcion_tecnologica + np.random.normal(0, 10, n_instituciones) + 5
    reduccion_tiempo = np.clip(reduccion_tiempo, 15, 85)

    # Tamaños basados en el tamaño de la institución
    tamanio_institucion = np.random.randint(500, 5000, n_instituciones)

    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(adopcion_tecnologica, reduccion_tiempo, s=tamanio_institucion/50,
                         c=tamanio_institucion, cmap='plasma', alpha=0.7, edgecolors='black', linewidth=0.5)

    # Línea de tendencia
    z = np.polyfit(adopcion_tecnologica, reduccion_tiempo, 1)
    p = np.poly1d(z)
    plt.plot(adopcion_tecnologica, p(adopcion_tecnologica), "--", color='red', linewidth=2, alpha=0.8)

    plt.xlabel('Adopción Tecnológica (%)')
    plt.ylabel('Reducción de Tiempo Administrativo (%)')
    plt.title('Correlación entre Adopción Tecnológica y Eficiencia Operativa')

    # Colorbar para tamaño de institución
    cbar = plt.colorbar(scatter)
    cbar.set_label('Tamaño de Institución (estudiantes)')

    # Añadir estadísticas
    correlation = np.corrcoef(adopcion_tecnologica, reduccion_tiempo)[0,1]
    plt.text(0.05, 0.95, f'Correlación: r = {correlation:.3f}',
             transform=plt.gca().transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/correlacion_tecnologias.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/correlacion_tecnologias.png', format='png')
    plt.close()
    print("✓ Generada: correlacion_tecnologias.pdf/png")

def generar_comparacion_tecnologias():
    """Genera gráfica de radar comparando tecnologías de identificación"""

    # Datos para comparación de tecnologías
    categorias = ['Facilidad\nUso', 'Velocidad\nAcceso', 'Costo\nImplementación', 'Seguridad\nDatos',
                  'Escalabilidad', 'Resistencia\nDaños']

    # Puntuaciones (1-10) para cada tecnología
    qr_scores = [9, 8, 7, 6, 9, 7]
    rfid_scores = [8, 9, 8, 8, 8, 9]
    biometrico_scores = [7, 10, 9, 10, 7, 10]

    # Configurar gráfica de radar
    angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
    angles += angles[:1]  # Cerrar el círculo

    qr_scores += qr_scores[:1]
    rfid_scores += rfid_scores[:1]
    biometrico_scores += biometrico_scores[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    # Dibujar las líneas para cada tecnología
    ax.plot(angles, qr_scores, 'o-', linewidth=2, label='Código QR', color='#2E86AB')
    ax.fill(angles, qr_scores, alpha=0.25, color='#2E86AB')

    ax.plot(angles, rfid_scores, 's-', linewidth=2, label='RFID', color='#F18F01')
    ax.fill(angles, rfid_scores, alpha=0.25, color='#F18F01')

    ax.plot(angles, biometrico_scores, '^-', linewidth=2, label='Biométrico', color='#C73E1D')
    ax.fill(angles, biometrico_scores, alpha=0.25, color='#C73E1D')

    # Configurar etiquetas y límites
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias)
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticklabels(range(0, 11, 2))
    ax.grid(True)

    plt.title('Comparación de Tecnologías de Identificación Digital', size=14, y=1.08)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/comparacion_tecnologias.pdf', format='pdf', bbox_inches='tight')
    plt.savefig(f'{graphics_dir}/comparacion_tecnologias.png', format='png', bbox_inches='tight')
    plt.close()
    print("✓ Generada: comparacion_tecnologias.pdf/png")

def generar_tabla_tecnologias():
    """Genera una tabla LaTeX con comparación de tecnologías de identificación"""

    tabla_latex = r"""
\begin{table}[htbp]
\centering
\caption{Comparación de Tecnologías de Identificación Digital}
\label{tab:tecnologias}
\begin{tabular}{lccccc}
\toprule
\textbf{Tecnología} & \textbf{Costo Inicial} & \textbf{Mantenimiento} & \textbf{Seguridad} & \textbf{Usabilidad} & \textbf{Puntuación} \\
\midrule
Código QR & Bajo & Muy Bajo & Media & Alta & 8.5 \\
RFID & Medio & Bajo & Alta & Alta & 8.8 \\
Biométrico & Alto & Alto & Muy Alta & Media & 9.2 \\
NFC & Medio & Bajo & Alta & Muy Alta & 8.9 \\
Tarjeta Magnética & Bajo & Medio & Baja & Alta & 7.1 \\
\bottomrule
\end{tabular}
\end{table}
"""

    # Guardar tabla en archivo
    with open(f'tables/tecnologias_comparison.tex', 'w', encoding='utf-8') as f:
        f.write(tabla_latex.strip())

    print("✓ Generada: tecnologias_comparison.tex")

def main():
    """Función principal para generar todas las gráficas"""
    print("🎨 Generando gráficas para plantilla LaTeX...")
    print("=" * 50)
    
    try:
        generar_eficiencia_acceso()
        generar_adopcion_tecnologias()
        generar_correlacion_tecnologias()
        generar_comparacion_tecnologias()
        generar_tabla_tecnologias()
        
        print("=" * 50)
        print("✅ ¡Todas las gráficas y tablas fueron generadas exitosamente!")
        print("\nArchivos generados:")
        print("📊 Gráficas PDF (para LaTeX): graphics/")
        print("🖼️  Gráficas PNG (para vista previa): graphics/")
        print("📋 Tabla LaTeX: tables/tecnologias_comparison.tex")
        
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
        raise

if __name__ == "__main__":
    main()