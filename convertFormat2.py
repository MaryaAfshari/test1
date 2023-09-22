from pydub import AudioSegment

def convert_m4a_to_wav(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file, format='m4a')
        audio.export(output_file, format='wav')
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

# Example usage
input_file = '/mnt/disk1/data/voxceleb_2/dev/aac/id00012/21Uxsk56VDQ/00001.m4a'
output_file = '/mnt/disk1/data/voxceleb_2/dev/aac/id00012/21Uxsk56VDQ/00001.wav'

convert_m4a_to_wav(input_file, output_file)