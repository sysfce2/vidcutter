from .types import Format


PROPERTIES = {
    'ab-loop-a':                   (Format.STRING, 'rw'),
    'ab-loop-b':                   (Format.STRING, 'rw'),
    'aid':                         (Format.STRING, 'rw'),
    'af':                          (Format.NODE,   'rw'),
    'af-metadata':                 (Format.NODE,   'r'),
    'angle':                       (Format.INT64,  'rw'),
    # 'ao-mute':                     (Format.FLAG,   'rw'),
    # 'ao-volume':                   (Format.DOUBLE, 'rw'),
    'ass-force-margins':           (Format.FLAG,   'rw'),
    'ass-style-override':          (Format.STRING, 'rw'),
    'ass-vsfilter-aspect-compat':  (Format.FLAG,   'rw'),
    'audio':                       (Format.STRING, 'rw'), # alias for aid
    'audio-bitrate':               (Format.DOUBLE, 'r'),
    'audio-channels':              (Format.STRING, 'r'),
    'audio-codec':                 (Format.STRING, 'r'),
    'audio-codec-name':            (Format.STRING, 'r'),
    'audio-delay':                 (Format.DOUBLE, 'rw'),
    'audio-device':                (Format.STRING, 'rw'),
    'audio-device-list':           (Format.NODE,   'r'),
    'audio-format':                (Format.STRING, 'r'),
    'audio-out-detected-device':   (Format.STRING, 'r'),
    'audio-out-params':            (Format.NODE,   'r'),
    'audio-params':                (Format.NODE,   'r'),
    'audio-pts':                   (Format.DOUBLE, 'r'),
    'audio-samplerate':            (Format.INT64,  'r'),
    'audio-speed-correction':      (Format.DOUBLE, 'r'),
    'avsync':                      (Format.DOUBLE, 'r'),
    'balance':                     (Format.DOUBLE, 'rw'),
    'border':                      (Format.FLAG,   'rw'),
    'brightness':                  (Format.INT64,  'rw'),
    'cache':                       (Format.DOUBLE, 'r'),
    'cache-buffering-state':       (Format.DOUBLE, 'r'),
    'cache-size':                  (Format.INT64,  'rw'),
    'cache-free':                  (Format.INT64,  'r'),
    'cache-used':                  (Format.INT64,  'r'),
    'cache-speed':                 (Format.INT64,  'r'),
    'cache-idle':                  (Format.FLAG,   'r'),
    'chapter':                     (Format.INT64,  'rw'),
    'chapter-list':                (Format.NODE,   'r'),
    'chapter-metadata':            (Format.NODE,   'r'),
    'chapters':                    (Format.INT64,  'r'),
    'colormatrix':                 (Format.STRING, 'rw'),
    'colormatrix-input-range':     (Format.STRING, 'rw'),
    'colormatrix-primaries':       (Format.STRING, 'rw'),
    'container-fps':               (Format.DOUBLE, 'r'),
    'contrast':                    (Format.INT64,  'rw'),
    'core-idle':                   (Format.FLAG,   'r'),
    'current-ao':                  (Format.STRING, 'r'),
    'current-vo':                  (Format.STRING, 'r'),
    'cursor-autohide':             (Format.STRING, 'rw'),
    'decoder-frame-drop-count':    (Format.INT64,  'r'),
    'decoder-list':                (Format.NODE,   'r'),
    'deinterlace':                 (Format.STRING, 'rw'),
    'demuxer':                     (Format.STRING, 'r'),
    'demuxer-cache-duration':      (Format.DOUBLE, 'r'),
    'demuxer-cache-time':          (Format.DOUBLE, 'r'),
    'demuxer-cache-idle':          (Format.FLAG,   'r'),
    'demuxer-start-time':          (Format.DOUBLE, 'r'),
    'demuxer-via-network':         (Format.FLAG,   'r'),
    'dheight':                     (Format.INT64,  'r'),
    'disc-title':                  (Format.STRING, 'rw'),
    'disc-title-list':             (Format.NODE,   'r'),
    'disc-titles':                 (Format.INT64,  'r'),
    'display-fps':                 (Format.INT64,  'rw'),
    'display-names':               (Format.STRING, 'r'),
    'display-sync-active':         (Format.FLAG,   'r'),
    'drop-frame-count':            (Format.INT64,  'r'),
    'duration':                    (Format.DOUBLE, 'r'),
    'dvb-channel':                 (Format.STRING, 'w'),
    'dvb-channel-name':            (Format.STRING, 'rw'),
    'dwidth':                      (Format.INT64,  'r'),
    'edition':                     (Format.INT64,  'rw'),
    'edition-list':                (Format.NODE,   'r'),
    'editions':                    (Format.INT64,  'r'),
    'encoder-list':                (Format.NODE,   'r'),
    'eof-reached':                 (Format.FLAG,   'r'),
    'estimated-display-fps':       (Format.INT64,  'r'),
    'estimated-frame-count':       (Format.INT64,  'r'),
    'estimated-frame-number':      (Format.INT64,  'r'),
    'estimated-vf-fps':            (Format.DOUBLE, 'r'),
    'ffmpeg-version':              (Format.STRING, 'r'),
    'field-dominance':             (Format.STRING, 'rw'),
    'file-format':                 (Format.STRING, 'r'),
    'file-local-options':          (Format.NODE,   'r'),
    'file-size':                   (Format.INT64,  'r'),
    'filename':                    (Format.STRING, 'r'),
    'filtered-metadata':           (Format.NODE,   'r'),
    'fps':                         (Format.DOUBLE, 'r'),
    'frame-drop-count':            (Format.INT64,  'r'),
    'framedrop':                   (Format.STRING, 'rw'),
    'fullscreen':                  (Format.FLAG,   'rw'),
    'gamma':                       (Format.DOUBLE, 'rw'),
    'height':                      (Format.INT64,  'r'),
    'hr-seek':                     (Format.STRING, 'rw'),
    'hue':                         (Format.INT64,  'rw'),
    'hwdec':                       (Format.STRING, 'rw'),
    'hwdec-current':               (Format.STRING, 'r'),
    'hwdec-interop':               (Format.STRING, 'r'),
    'idle':                        (Format.FLAG,   'r'),
    'idle-active':                 (Format.FLAG,   'r'),
    'keepaspect':                  (Format.FLAG,   'r'),
    'length':                      (Format.DOUBLE, 'r'),
    'loop':                        (Format.STRING, 'rw'),
    'loop-file':                   (Format.STRING, 'rw'),
    'media-title':                 (Format.STRING, 'r'),
    'metadata':                    (Format.NODE,   'r'),
    'mistimed-frame-count':        (Format.INT64,  'r'),
    'mixer-active':                (Format.FLAG,   'r'),
    'mpv-configuration':           (Format.FLAG,   'r'),
    'mpv-version':                 (Format.STRING, 'r'),
    'mute':                        (Format.FLAG,   'rw'),
    'on-all-workspaces':           (Format.FLAG,   'rw'),  # X11 only
    'ontop':                       (Format.FLAG,   'rw'),
    'options':                     (Format.NODE,   'r'),
    # 'osd-ass-cc':                  (Format.STRING, 'r'),
    'osd-height':                  (Format.INT64,  'r'),
    'osd-level':                   (Format.INT64,  'rw'),
    'osd-par':                     (Format.DOUBLE, 'r'),
    'osd-scale':                   (Format.DOUBLE, 'rw'),
    # 'osd-sym-cc':                  (Format.STRING, 'r'),
    'osd-width':                   (Format.INT64,  'r'),
    'packet-audio-bitrate':        (Format.DOUBLE, 'r'),
    'packet-sub-bitrate':          (Format.DOUBLE, 'r'),
    'packet-video-bitrate':        (Format.DOUBLE, 'r'),
    'panscan':                     (Format.DOUBLE, 'rw'),
    'partially-seekable':          (Format.FLAG,   'r'),
    'path':                        (Format.STRING, 'r'),
    'pause':                       (Format.FLAG,   'rw'),
    'paused-for-cache':            (Format.FLAG,   'r'),
    'percent-pos':                 (Format.DOUBLE, 'rw'),
    'playback-abort':              (Format.FLAG,   'r'),
    'playback-time':               (Format.DOUBLE, 'rw'),
    'playlist':                    (Format.NODE,   'r'),
    'playlist-count':              (Format.INT64,  'r'),
    'playlist-pos':                (Format.INT64,  'rw'),
    'playlist-pos-1':              (Format.INT64,  'rw'),
    'playtime-remaining':          (Format.DOUBLE, 'r'),
    'profile-list':                (Format.NODE,   'r'),
    'program':                     (Format.INT64,  'w'),
    'property-list':               (Format.NODE,   'r'),
    'protocol-list':               (Format.NODE,   'r'),
    'saturation':                  (Format.INT64,  'rw'),
    'secondary-sid':               (Format.STRING, 'rw'),
    'seekable':                    (Format.FLAG,   'r'),
    'seeking':                     (Format.FLAG,   'r'),
    'sid':                         (Format.STRING, 'rw'),
    'speed':                       (Format.DOUBLE, 'rw'),
    'stream-capture':              (Format.STRING, 'rw'),
    'stream-end':                  (Format.INT64,  'r'),
    'stream-open-filename':        (Format.STRING, 'rw'),
    'stream-path':                 (Format.STRING, 'r'),
    'stream-pos':                  (Format.INT64,  'r'),
    'sub':                         (Format.STRING, 'rw'), # alias for sid
    'sub-bitrate':                 (Format.DOUBLE, 'r'),
    'sub-delay':                   (Format.DOUBLE, 'rw'),
    'sub-forced-only':             (Format.FLAG,   'rw'),
    'sub-pos':                     (Format.INT64,  'rw'),
    'sub-scale':                   (Format.DOUBLE, 'rw'),
    'sub-text':                    (Format.STRING, 'r'),
    'sub-use-margins':             (Format.FLAG,   'rw'),
    'sub-visibility':              (Format.FLAG,   'rw'),
    'taskbar-progress':            (Format.FLAG,   'rw'),
    'time-pos':                    (Format.DOUBLE, 'rw'),
    'time-remaining':              (Format.DOUBLE, 'r'),
    'time-start':                  (Format.DOUBLE, 'r'),  # deprecated
    'total-avsync-change':         (Format.DOUBLE, 'r'),
    'track-list':                  (Format.NODE,   'r'),
    'tv-brightness':               (Format.INT64,  'rw'),
    'tv-contrast':                 (Format.INT64,  'rw'),
    'tv-hue':                      (Format.INT64,  'rw'),
    'tv-saturation':               (Format.INT64,  'rw'),
    'vf':                          (Format.NODE,   'rw'),
    'vid':                         (Format.STRING, 'rw'),
    'video':                       (Format.STRING, 'rw'), # alias for vid
    'video-align-x':               (Format.DOUBLE, 'rw'),
    'video-align-y':               (Format.DOUBLE, 'rw'),
    'video-aspect':                (Format.STRING, 'rw'),
    'video-bitrate':               (Format.DOUBLE, 'r'),
    'video-codec':                 (Format.STRING, 'r'),
    'video-dec-params':            (Format.NODE,   'r'),
    'video-format':                (Format.STRING, 'r'),
    'video-frame-info':            (Format.NODE,   'r'),
    'video-out-params':            (Format.NODE,   'r'),
    'video-output-levels':         (Format.STRING, 'rw'),
    'video-pan-x':                 (Format.INT64,  'rw'),
    'video-pan-y':                 (Format.INT64,  'rw'),
    'video-params':                (Format.NODE,   'r'),
    'video-rotate':                (Format.STRING, 'rw'),
    'video-speed-correction':      (Format.DOUBLE, 'r'),
    'video-stereo-mode':           (Format.STRING, 'rw'),
    'video-unscaled':              (Format.FLAG,   'w'),
    'video-zoom':                  (Format.DOUBLE, 'rw'),
    'vf-metadata':                 (Format.NODE,   'r'),
    'vo-configured':               (Format.FLAG,   'r'),
    'vo-delayed-frame-count':      (Format.INT64,  'r'),
    'vo-drop-frame-count':         (Format.INT64,  'r'),
    'vo-performance':              (Format.NODE,   'r'),
    'volume':                      (Format.DOUBLE, 'rw'),
    'volume-max':                  (Format.DOUBLE, 'rw'),
    'vsync-jitter':                (Format.DOUBLE, 'r'),
    'vsync-ratio':                 (Format.DOUBLE, 'r'),
    'width':                       (Format.INT64,  'r'),
    'window-minimized':            (Format.FLAG,   'r'),
    'window-scale':                (Format.DOUBLE, 'rw'),
    'working-directory':           (Format.STRING, 'r')
}
"""dict: properties.
"""
