"""
    Unlocke

    Copyright (C) 2020  Errite Games LLC/ ErriteEpticRikez
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from nacl.public import PublicKey, PrivateKey, SealedBox

with open("./private.key", "rb") as f:
    priv_byte = f.read()
    with open("./public.key", "rb") as pubf:
        pubf_byte = pubf.read()
        public_key = PublicKey(pubf_byte)
        private_key = PrivateKey(priv_byte)
        test_message = "This a test message!"
        sealed_box = SealedBox(public_key)
        encrypted_text = sealed_box.encrypt(bytes(test_message,"utf-8"))
        unseal = SealedBox(private_key)

        result = unseal.decrypt(encrypted_text)
        print(result.decode("utf-8"))

