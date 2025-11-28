#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Gráficas para Plantilla LaTeX - Ingeniería de Software
Genera gráficas de ejemplo relacionadas con DevOps, metodologías ágiles y métricas DORA
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

def generar_metricas_dora():
    """Genera gráfica de barras con tiempo promedio de acceso y precisión de identificación"""

    # Datos de métodos de identificación
    metodos = ['Manual\n(Papel)', 'Tarjeta\nRFID', 'Código\nQR', 'Biométrico']
    tiempo_acceso = [45.2, 2.1, 3.8, 1.5]  # segundos
    precision = [85, 98, 95, 99]  # porcentaje

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Gráfica 1: Tiempo promedio de acceso
    bars1 = ax1.bar(metodos, tiempo_acceso, color=['#C73E1D', '#F18F01', '#2E86AB', '#A23B72'])
    ax1.set_title('Tiempo Promedio de Acceso')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_ylim(0, 50)

    # Añadir valores en las barras
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}s', ha='center', va='bottom')

    # Gráfica 2: Precisión de identificación
    bars2 = ax2.bar(metodos, precision, color=['#C73E1D', '#F18F01', '#2E86AB', '#A23B72'])
    ax2.set_title('Precisión de Identificación')
    ax2.set_ylabel('Precisión (%)')
    ax2.set_ylim(0, 100)

    # Añadir valores en las barras
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}\%', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/metricas_dora.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/metricas_dora.png', format='png')
    plt.close()
    print("✓ Generada: metricas_dora.pdf/png")

def generar_evolucion_temporal():
    """Genera gráfica de líneas mostrando evolución de la adopción tecnológica"""

    # Datos de ejemplo: evolución mensual de adopción
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
    adopcion_qr = [10, 15, 20, 28, 35, 42, 50, 58, 65, 72, 78, 82]
    adopcion_rfid = [5, 8, 12, 18, 25, 32, 40, 48, 55, 62, 68, 73]
    usuarios_totales = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1850, 1900, 1950]

    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Eje Y izquierdo: Adopción tecnológica
    color = '#2E86AB'
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Adopción Tecnológica (\%)', color=color)
    line1 = ax1.plot(meses, adopcion_qr, color=color, marker='o', linewidth=2,
                     label='Adopción Código QR (\%)')
    line2 = ax1.plot(meses, adopcion_rfid, color='#F18F01', marker='s', linewidth=2,
                     label='Adopción RFID (\%)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 100)

    # Eje Y derecho: Usuarios totales
    ax2 = ax1.twinx()
    color = '#C73E1D'
    ax2.set_ylabel('Usuarios Registrados', color=color)
    line3 = ax2.plot(meses, usuarios_totales, color=color, marker='^', linewidth=2,
                     label='Usuarios Totales')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(900, 2000)

    # Leyenda combinada
    lines = line1 + line2 + line3
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')

    plt.title('Evolución de la Adopción de Tecnologías QR y RFID (2024)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/evolucion_metricas.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/evolucion_metricas.png', format='png')
    plt.close()
    print("✓ Generada: evolucion_metricas.pdf/png")

def generar_correlacion_practicas():
    """Genera gráfica de dispersión mostrando correlación entre adopción tecnológica y eficiencia"""

    np.random.seed(42)  # Para reproducibilidad

    # Datos simulados: correlación entre adopción tecnológica y reducción de tiempo administrativo
    n_instituciones = 25
    adopcion = np.random.normal(60, 20, n_instituciones)
    adopcion = np.clip(adopcion, 30, 90)

    # Correlación positiva con algo de ruido (r ≈ 0.824)
    reduccion_tiempo = 0.824 * (adopcion - 30) + np.random.normal(0, 8, n_instituciones) + 20
    reduccion_tiempo = np.clip(reduccion_tiempo, 20, 70)

    # Tamaños basados en el tamaño de la institución
    institution_sizes = np.random.randint(1000, 5000, n_instituciones)

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(adopcion, reduccion_tiempo, s=institution_sizes/100,
                         c=institution_sizes, cmap='viridis', alpha=0.7, edgecolors='black', linewidth=0.5)

    # Línea de tendencia
    z = np.polyfit(adopcion, reduccion_tiempo, 1)
    p = np.poly1d(z)
    plt.plot(adopcion, p(adopcion), "--", color='red', linewidth=2, alpha=0.8)

    plt.xlabel('Adopción Tecnológica (\%)')
    plt.ylabel('Reducción de Tiempo Administrativo (\%)')
    plt.title('Correlación entre Adopción Tecnológica y Eficiencia Operativa')

    # Colorbar para tamaño de la institución
    cbar = plt.colorbar(scatter)
    cbar.set_label('Tamaño de Institución (estudiantes)')

    # Añadir estadísticas
    correlation = np.corrcoef(adopcion, reduccion_tiempo)[0,1]
    plt.text(0.05, 0.95, f'Correlación: r = {correlation:.3f}',
             transform=plt.gca().transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/correlacion_devops.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/correlacion_devops.png', format='png')
    plt.close()
    print("✓ Generada: correlacion_devops.pdf/png")

def generar_comparacion_metodologias():
    """Genera gráfica de radar comparando tecnologías de identificación digital"""

    # Datos para comparación de tecnologías
    categorias = ['Facilidad\nUso', 'Velocidad', 'Acceso', 'Costo', 'Implementación',
                  'Seguridad', 'Datos', 'Escalabilidad', 'Resistencia\nDaños']

    # Puntuaciones (0-10) para cada tecnología
    qr_scores = [8, 9, 7, 9, 8, 6, 7, 8, 7]
    rfid_scores = [7, 10, 9, 7, 7, 8, 8, 9, 8]
    bio_scores = [5, 9, 10, 4, 5, 10, 9, 7, 9]

    # Configurar gráfica de radar
    angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
    angles += angles[:1]  # Cerrar el círculo

    qr_scores += qr_scores[:1]
    rfid_scores += rfid_scores[:1]
    bio_scores += bio_scores[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))

    # Dibujar las líneas para cada tecnología
    ax.plot(angles, qr_scores, 'o-', linewidth=2, label='Código QR', color='#2E86AB')
    ax.fill(angles, qr_scores, alpha=0.25, color='#2E86AB')

    ax.plot(angles, rfid_scores, 's-', linewidth=2, label='RFID', color='#F18F01')
    ax.fill(angles, rfid_scores, alpha=0.25, color='#F18F01')

    ax.plot(angles, bio_scores, '^-', linewidth=2, label='Biométrico', color='#C73E1D')
    ax.fill(angles, bio_scores, alpha=0.25, color='#C73E1D')

    # Configurar etiquetas y límites
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias)
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticklabels(range(0, 11, 2))
    ax.grid(True)

    plt.title('Comparación multi-criterio de tecnologías de identificación digital', size=14, y=1.08)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/comparacion_metodologias.pdf', format='pdf', bbox_inches='tight')
    plt.savefig(f'{graphics_dir}/comparacion_metodologias.png', format='png', bbox_inches='tight')
    plt.close()
    print("✓ Generada: comparacion_metodologias.pdf/png")

def generar_tabla_frameworks():
    """Genera una tabla LaTeX con comparación de tecnologías de identificación"""

    tabla_latex = r"""
\begin{table}[htbp]
\centering
\caption{Comparación de Tecnologías de Identificación Digital}
\label{tab:frameworks}
\begin{tabular}{lcccc}
\toprule
\textbf{Tecnología} & \textbf{Costo Inicial} & \textbf{Mantenimiento} & \textbf{Seguridad} & \textbf{Usabilidad} \\
\midrule
Código QR & Bajo & Muy Bajo & Media & Alta \\
RFID & Medio & Bajo & Alta & Alta \\
NFC & Medio & Bajo & Alta & Muy Alta \\
Tarjeta Magnética & Bajo & Medio & Baja & Alta \\
\bottomrule
\end{tabular}
\end{table}
"""

    # Guardar tabla en archivo
    with open(f'tables/frameworks_comparison.tex', 'w', encoding='utf-8') as f:
        f.write(tabla_latex.strip())

    print("✓ Generada: frameworks_comparison.tex")

def main():
    """Función principal para generar todas las gráficas"""
    print("🎨 Generando gráficas para plantilla LaTeX...")
    print("=" * 50)
    
    try:
        generar_metricas_dora()
        generar_evolucion_temporal()
        generar_correlacion_practicas()
        generar_comparacion_metodologias()
        generar_tabla_frameworks()
        
        print("=" * 50)
        print("✅ ¡Todas las gráficas y tablas fueron generadas exitosamente!")
        print("\nArchivos generados:")
        print("📊 Gráficas PDF (para LaTeX): graphics/")
        print("🖼️  Gráficas PNG (para vista previa): graphics/")
        print("📋 Tabla LaTeX: tables/frameworks_comparison.tex")
        
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
        raise

if __name__ == "__main__":
    main()