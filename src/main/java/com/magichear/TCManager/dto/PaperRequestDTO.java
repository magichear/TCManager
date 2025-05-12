package com.magichear.TCManager.dto;

import lombok.Data;
import java.util.List;

@Data
public class PaperRequestDTO {
    private PaperDTO paper;
    private List<PublishPaperResponseDTO> authors;
}