import soundfile as sf

def convert_m4a_to_wav(input_file, output_file):
    try:
        data, samplerate = sf.read(input_file)
        sf.write(output_file, data, samplerate, format='WAV')
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

# Example usage
input_file = '/mnt/disk1/data/voxceleb_2/dev/aac/id00012/21Uxsk56VDQ/00001.m4a'    # Specify the input .m4a file path
output_file = '/mnt/disk1/data/voxceleb_2/dev/aac/id00012/21Uxsk56VDQ/00001.wav'  # Specify the output .wav file path

convert_m4a_to_wav(input_file, output_file)