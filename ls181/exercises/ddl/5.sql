ALTER TABLE stars ADD CONSTRAINT type_check CHECK (spectral_type IN ('O', 'B', 'A', 'F', 'G', 'K', 'M')),

ALTER COLUMN spectral_type SET NOT NULL;