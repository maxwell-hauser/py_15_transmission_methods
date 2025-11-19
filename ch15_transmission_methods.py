#!/usr/bin/env python3
"""
Chapter 15: Transmission Methods (Serial vs Parallel)
Demonstrates serial and parallel data transmission
"""

def visualize_parallel_transmission(byte):
    """Visualize parallel transmission"""
    print(f"\nParallel Transmission: {byte}")
    print("\nAll 8 bits transmitted simultaneously:")
    print()
    print("Bit 7 ─────────────────────► " + byte[0])
    print("Bit 6 ─────────────────────► " + byte[1])
    print("Bit 5 ─────────────────────► " + byte[2])
    print("Bit 4 ─────────────────────► " + byte[3])
    print("Bit 3 ─────────────────────► " + byte[4])
    print("Bit 2 ─────────────────────► " + byte[5])
    print("Bit 1 ─────────────────────► " + byte[6])
    print("Bit 0 ─────────────────────► " + byte[7])
    print()
    print("8 wires, 1 time unit")

def visualize_serial_transmission(byte):
    """Visualize serial transmission"""
    print(f"\nSerial Transmission: {byte}")
    print("\nBits transmitted one at a time:")
    print()
    
    timeline = "Time: "
    wire = "Wire: "
    
    for i, bit in enumerate(byte):
        timeline += f"T{i} "
        wire += f"{bit}  "
    
    print(timeline)
    print(wire)
    print()
    print("1 wire, 8 time units")

def calculate_transmission_time(bits, wires, bit_rate):
    """Calculate transmission time"""
    if wires == 1:
        # Serial: transmit bits one at a time
        time_per_bit = 1 / bit_rate
        total_time = bits * time_per_bit
    else:
        # Parallel: transmit all bits simultaneously
        time_per_bit = 1 / bit_rate
        total_time = time_per_bit
    
    return total_time

def compare_transmission_methods(data_bytes, bit_rate=1_000_000):
    """Compare serial vs parallel for multiple bytes"""
    bits = data_bytes * 8
    
    # Serial transmission
    serial_time = calculate_transmission_time(bits, 1, bit_rate)
    serial_wires = 1
    
    # Parallel transmission (8 wires)
    parallel_time = calculate_transmission_time(8, 8, bit_rate) * data_bytes
    parallel_wires = 8
    
    print(f"\nTransmitting {data_bytes} bytes ({bits} bits) at {bit_rate:,} bps:")
    print()
    print(f"Serial Transmission:")
    print(f"  Wires:         {serial_wires}")
    print(f"  Time:          {serial_time * 1000:.3f} ms")
    print(f"  Bits/transfer: 1")
    
    print(f"\nParallel Transmission:")
    print(f"  Wires:         {parallel_wires}")
    print(f"  Time:          {parallel_time * 1000:.3f} ms")
    print(f"  Bits/transfer: 8")
    
    speedup = serial_time / parallel_time
    print(f"\nSpeedup: {speedup:.1f}x faster")
    print(f"Cost: {parallel_wires}x more wires")

def main():
    print("=" * 60)
    print("CHAPTER 15: Transmission Methods")
    print("Serial vs Parallel Transmission")
    print("=" * 60)
    
    # Example 1: Parallel Transmission
    print("\n--- Example 1: Parallel Transmission ---")
    print("\nDefinition: Multiple bits transmitted simultaneously")
    print("over multiple wires (one wire per bit).")
    
    byte = "10110101"
    visualize_parallel_transmission(byte)
    
    # Example 2: Serial Transmission
    print("\n--- Example 2: Serial Transmission ---")
    print("\nDefinition: Bits transmitted one at a time")
    print("over a single wire.")
    
    byte = "10110101"
    visualize_serial_transmission(byte)
    
    # Example 3: Comparison for 1 byte
    print("\n--- Example 3: Transmission Comparison (1 byte) ---")
    
    print("\nParallel (8 wires):")
    print("  T0: 1 0 1 1 0 1 0 1  ← All 8 bits at once")
    print("  ═══════════════════")
    print("  Time units: 1")
    
    print("\nSerial (1 wire):")
    print("  T0: 1")
    print("  T1: 0")
    print("  T2: 1")
    print("  T3: 1")
    print("  T4: 0")
    print("  T5: 1")
    print("  T6: 0")
    print("  T7: 1")
    print("  ═══")
    print("  Time units: 8")
    
    # Example 4: Multi-byte Transmission
    print("\n--- Example 4: Multiple Byte Transmission ---")
    compare_transmission_methods(1, 1_000_000)
    print()
    compare_transmission_methods(100, 1_000_000)
    
    # Example 5: Bus Width
    print("\n--- Example 5: Parallel Bus Widths ---")
    
    bus_widths = [
        (8, "Early computer buses (ISA)"),
        (16, "PC expansion bus"),
        (32, "PCI, modern memory buses"),
        (64, "Modern CPU to memory"),
        (128, "Graphics card memory"),
        (256, "High-end GPU memory")
    ]
    
    print("\nCommon parallel bus widths:")
    print("Bits | Application")
    print("-----|----------------------------------")
    for width, application in bus_widths:
        print(f"{width:4d} | {application}")
    
    print("\nWider bus = more data per clock cycle")
    print("But requires more physical wires!")
    
    # Example 6: Advantages and Disadvantages
    print("\n--- Example 6: Trade-offs ---")
    
    print("\nParallel Transmission:")
    print("  Advantages:")
    print("    ✓ Faster (transmits multiple bits at once)")
    print("    ✓ Good for short distances")
    print("    ✓ Simple timing (no serialization needed)")
    
    print("  Disadvantages:")
    print("    ✗ More wires required (expensive)")
    print("    ✗ Crosstalk between wires")
    print("    ✗ Skew: bits may arrive at different times")
    print("    ✗ Not practical for long distances")
    print("    ✗ More complex connectors")
    
    print("\nSerial Transmission:")
    print("  Advantages:")
    print("    ✓ Fewer wires (cheaper)")
    print("    ✓ Suitable for long distances")
    print("    ✓ Less crosstalk")
    print("    ✓ Simpler cables and connectors")
    print("    ✓ Can achieve very high speeds")
    
    print("  Disadvantages:")
    print("    ✗ Slower per wire (one bit at a time)")
    print("    ✗ Requires serialization/deserialization")
    print("    ✗ More complex circuitry")
    
    # Example 7: Real-world Examples
    print("\n--- Example 7: Real-world Interfaces ---")
    
    print("\nParallel Interfaces (legacy):")
    parallel_examples = [
        ("Parallel Port (LPT)", "8 data lines", "Printer connection"),
        ("IDE/PATA", "16-bit", "Hard drives"),
        ("PCI", "32/64-bit", "Expansion cards"),
        ("Memory Bus", "64-256 bit", "RAM connection")
    ]
    
    for name, width, use in parallel_examples:
        print(f"  • {name:20s} {width:12s} - {use}")
    
    print("\nSerial Interfaces (modern):")
    serial_examples = [
        ("USB", "Up to 40 Gbps", "Universal connection"),
        ("SATA", "6 Gbps", "Hard drives/SSDs"),
        ("PCIe", "32 GT/s per lane", "GPUs, NVMe SSDs"),
        ("Ethernet", "10 Gbps+", "Networking"),
        ("HDMI", "48 Gbps", "Video/audio"),
        ("Thunderbolt", "40 Gbps", "High-speed peripherals")
    ]
    
    for name, speed, use in serial_examples:
        print(f"  • {name:20s} {speed:15s} - {use}")
    
    # Example 8: The Modern Shift
    print("\n--- Example 8: Why Serial Won ---")
    
    print("\nHistorical trend: Parallel → Serial")
    print("\nReasons:")
    print("  1. Clock Skew: At high speeds, parallel signals")
    print("     arrive at different times (skew)")
    
    print("\n  2. Cost: Fewer wires = cheaper cables")
    
    print("\n  3. Technology: Modern serial can be FASTER")
    print("     - USB 3.0: 5 Gbps")
    print("     - Old parallel port: 2 Mbps")
    print("     Serial is 2500x faster!")
    
    print("\n  4. Distance: Serial works over longer cables")
    
    print("\n  5. Scalability: Easier to increase serial speed")
    print("     than add more parallel wires")
    
    # Example 9: Transmission Calculation
    print("\n--- Example 9: Speed Calculation ---")
    
    scenarios = [
        ("Send 1 MB over USB 2.0 (480 Mbps)", 1024*1024*8, 480_000_000),
        ("Send 1 MB over USB 3.0 (5 Gbps)", 1024*1024*8, 5_000_000_000),
        ("Send 1 MB over old parallel (2 Mbps)", 1024*1024*8, 2_000_000)
    ]
    
    print("\nTransmission time comparison:")
    for desc, bits, bitrate in scenarios:
        time_seconds = bits / bitrate
        if time_seconds < 1:
            time_str = f"{time_seconds * 1000:.1f} ms"
        else:
            time_str = f"{time_seconds:.2f} seconds"
        
        print(f"\n{desc}")
        print(f"  Time: {time_str}")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Parallel: Multiple bits simultaneously, multiple wires")
    print("- Serial: One bit at a time, single wire")
    print("- Parallel: Faster per clock, but limited by skew")
    print("- Serial: Fewer wires, better for long distance")
    print("- Modern trend: Serial interfaces dominate")
    print("- High-speed serial > low-speed parallel")
    print("=" * 60)

if __name__ == "__main__":
    main()
